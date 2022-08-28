import json
from pathlib import Path
from utils.configuration import Storage, args_from_config, generate_td_py_arguments
from pipeline.pipeline import Pipeline

args = generate_td_py_arguments().parse_known_args()[0]
parameters = Storage()

try:
    configuration_path = args.config
    parameters: Storage = args_from_config(configuration_path, 'TRAINING DATA')
except AttributeError:
    pass

# Override with arguments
for k, v in args.__dict__.items():
    parameters.__setattr__(k, v)

OUTPUT_PATH = parameters.output_path
OUTPUT_NAME = parameters.output_name

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

p = Pipeline(input_path=parameters.input_path, seed=parameters.seed, data_size=parameters.data_size, examples_per_task=parameters.examples_per_task,
             min_list_length=parameters.min_list_length, max_list_length=parameters.max_list_length, tab_length=parameters.tab_length)
tasks, language, vocab = p.generate_data_shuffled()

with open(train_data_path + "/tasks.json", "w") as outfile:
    json.dump(tasks, outfile)
with open(train_language_data_path + "/language.json", "w") as outfile:
    json.dump(language, outfile)
with open(train_language_data_path + "/vocab.json", "w") as outfile:
    json.dump(vocab, outfile)

p = Pipeline(input_path=parameters.input_path, seed=parameters.seed+1, data_size=parameters.data_size, examples_per_task=parameters.examples_per_task,
             min_list_length=parameters.min_list_length, max_list_length=parameters.max_list_length, tab_length=parameters.tab_length)
tasks, language, vocab = p.generate_data_shuffled()

with open(test_data_path + "/tasks.json", "w") as outfile:
    json.dump(tasks, outfile)
with open(test_language_data_path + "/language.json", "w") as outfile:
    json.dump(language, outfile)
with open(test_language_data_path + "/vocab.json", "w") as outfile:
    json.dump(vocab, outfile)
