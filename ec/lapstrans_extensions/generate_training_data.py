import json
from pathlib import Path
from configuration import generate_td_py_arguments
from pipeline.pipeline import Pipeline

args = generate_td_py_arguments()

OUTPUT_PATH = args.output_path
OUTPUT_NAME = args.output_name

train_data_path = f"{OUTPUT_PATH}/tasks/{OUTPUT_NAME}/train"
train_language_data_path = f"{OUTPUT_PATH}/language/{OUTPUT_NAME}/train"
test_data_path = f"{OUTPUT_PATH}/tasks/{OUTPUT_NAME}/test"
test_language_data_path = f"{OUTPUT_PATH}/language/{OUTPUT_NAME}/test"
for path in [
    train_data_path,
    train_language_data_path,
    test_data_path,
    test_language_data_path,
]:
    Path(path).mkdir(parents=True, exist_ok=True)

p = Pipeline(input_path=args.input_path, seed=args.seed, data_size=args.data_size, examples_per_task=args.examples_per_task,
             min_list_length=args.min_list_length, max_list_length=args.max_list_length, tab_length=args.tab_length)
tasks, language, vocab = p.generate_data_shuffled()

with open(train_data_path + "/tasks.json", "w") as outfile:
    json.dump(tasks, outfile)
with open(train_language_data_path + "/language.json", "w") as outfile:
    json.dump(language, outfile)
with open(train_language_data_path + "/vocab.json", "w") as outfile:
    json.dump(vocab, outfile)

p = Pipeline(input_path=args.input_path, seed=args.seed+1, data_size=args.data_size, examples_per_task=args.examples_per_task,
             min_list_length=args.min_list_length, max_list_length=args.max_list_length, tab_length=args.tab_length)
tasks, language, vocab = p.generate_data_shuffled()

with open(test_data_path + "/tasks.json", "w") as outfile:
    json.dump(tasks, outfile)
with open(test_language_data_path + "/language.json", "w") as outfile:
    json.dump(language, outfile)
with open(test_language_data_path + "/vocab.json", "w") as outfile:
    json.dump(vocab, outfile)
