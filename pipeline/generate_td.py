import json
from pathlib import Path
from pipeline import Pipeline

OUTPUT_PATH = "./ec/data/list"
DATASET_NAME = "list_20"

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

p = Pipeline("pipeline/f_file.py")
tasks, language, vocab = p.generate_data_shuffled()

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
