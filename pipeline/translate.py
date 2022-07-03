import json
from pathlib import Path
import subprocess
import sys
from pipeline import Pipeline

OUTPUT_PATH = "./ec/data/list"
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

p = Pipeline(sys.argv[1])
tasks, language, vocab = p.generate_data_strict()

with open(train_data_path + "/tasks.json", "w") as outfile:
    json.dump(tasks, outfile)
with open(train_data_path + "/language.json", "w") as outfile:
    json.dump(language, outfile)
with open(train_data_path + "/vocab.json", "w") as outfile:
    json.dump(vocab, outfile)

with open(test_data_path + "/tasks.json", "w") as outfile:
    json.dump(tasks, outfile)
with open(test_language_data_path + "/language.json", "w") as outfile:
    json.dump(language, outfile)
with open(test_language_data_path + "/vocab.json", "w") as outfile:
    json.dump(vocab, outfile)

print('Solved tasks are written to the data folder.\n')

laps_command = [
    "python3",
    "bin/list.py",
    "--enumerationTimeout",
    "10",
    "--testingTimeout",
    "0",
    "--iterations",
    "100",
    "--biasOptimal",
    "--contextual",
    "--taskBatchSize",
    str(len(tasks)),
    #"--testEvery",
    #"3",
    "--no-cuda",
    "--recognitionTimeout",
    "10",
    "--recognition_0",
    "examples",
    "--Helmholtz",
    "0.5",
    "--skip_first_test",
    "--taskDataset",
    DATASET_NAME,
    "--translate"
]

subprocess.run(laps_command, capture_output=True, text=True, cwd='./ec/')