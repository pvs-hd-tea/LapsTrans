from argparse import ArgumentError
import os
from utils.configuration import Storage, args_from_config, translate_py_arguments
from pipeline.pipeline import Pipeline
from pathlib import Path
import json

TMP_INPUT_FILE = "lapstrans_extensions/working_dir/cli_input.py"
args = translate_py_arguments().parse_known_args()[0]

parameters = Storage()

try:
    configuration_path = args.config
    parameters: Storage = args_from_config(configuration_path, 'TRANSLATE')
except AttributeError:
    pass

# Override with arguments
for k, v in args.__dict__.items():
    if v is not None:
        parameters.__setattr__(k, v)


# Resolve input
if parameters.cli:
    parameters.input_file = TMP_INPUT_FILE
    print("Running with --cli parameter, please enter the function to translate.\n")
    with open(parameters.input_file, "w") as f:
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
    parameters.input_file = parameters.input_path

CHECKPOINT_PATH = parameters.checkpoint_path
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

p = Pipeline(input_path=parameters.input_file, seed=parameters.seed,
             examples_per_task=parameters.examples_per_task, min_list_length=parameters.min_list_length, max_list_length=parameters.max_list_length, tab_length=parameters.tab_length)
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
