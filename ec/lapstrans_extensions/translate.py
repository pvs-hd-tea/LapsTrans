import os
from lapstrans_extensions.utils.configuration import translate_py_arguments
from pipeline.pipeline import Pipeline
from pathlib import Path
import json

TMP_INPUT_FILE = "lapstrans_extensions/working_dir/cli_input.py"
args = translate_py_arguments()
try:
    cli = args.cli
except:
    cli = False

# Resolve input
if cli:
    input_file = TMP_INPUT_FILE
    print("Running with --cli parameter, please enter the function to translate.\n")
    with open(input_file, "w") as f:
        recording = True
        one_stop = True
        while recording:
            line = input()
            f.write(line)
            if line == '':
                if one_stop:
                    recording = False
                else:
                    one_stop = True
                    print('Define next function, or press ENTER again to finish.\n')
            else:
                one_stop = False
else:
    input_file = args.input_path

CHECKPOINT_PATH = args.checkpoint_path
OUTPUT_PATH = "./data/list"
DATASET_NAME = "list_to_translate"

train_data_path = f"{OUTPUT_PATH}/tasks/{DATASET_NAME}/train"
train_language_data_path = f"{OUTPUT_PATH}/language/{DATASET_NAME}/train"
test_data_path = f"{OUTPUT_PATH}/tasks/{DATASET_NAME}/test"
test_language_data_path = f"{OUTPUT_PATH}/language/{DATASET_NAME}/test"
for path in [
    train_data_path,
    train_language_data_path,
    test_data_path,
    test_language_data_path,
]:
    Path(path).mkdir(parents=True, exist_ok=True)

p = Pipeline(input_path=input_file, seed=args.seed,
             examples_per_task=args.examples_per_task, min_list_length=args.min_list_length, max_list_length=args.max_list_length, tab_length=args.tab_length)
tasks, language, vocab = p.generate_data_strict()

with open(train_data_path + "/tasks.json", "w") as outfile:
    json.dump(tasks, outfile)
with open(train_language_data_path + "/language.json", "w") as outfile:
    json.dump(language, outfile)
with open(train_language_data_path + "/vocab.json", "w") as outfile:
    json.dump(vocab, outfile)

with open(test_data_path + "/tasks.json", "w") as outfile:
    json.dump(tasks, outfile)
with open(test_language_data_path + "/language.json", "w") as outfile:
    json.dump(language, outfile)
with open(test_language_data_path + "/vocab.json", "w") as outfile:
    json.dump(vocab, outfile)

print('Solved tasks are written to the data folder.\n')

laps_command = [
    "python3.7",
    "bin/list.py",
    "--resume",
    CHECKPOINT_PATH,
    "--taskDataset",
    DATASET_NAME,
    "--iterations",
    "100",
    "--enumerationTimeout",
    "30",
    "--translate",
    "--no-cuda",
    "--Helmholtz",
    "0"
]

laps_command = ' '.join(laps_command)

process = os.popen(laps_command)
for line in process.readlines():
    pass
print("Translation attempt finished, the results are accessible at lapstrans_extensions/working_dir/translation.json")
