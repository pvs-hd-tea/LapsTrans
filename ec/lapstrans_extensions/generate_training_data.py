import json
from pathlib import Path
from pipeline.pipeline import Pipeline
import argparse

parser = argparse.ArgumentParser(
    description='Generate training data for LapsTrans project.')
parser.add_argument(
    '-d', '--datapath', help='path of the file with functions used for training', type=str, required=True)
parser.add_argument('-p', '--path', help='Custom output path. Default: ./data/list/',
                    default="./data/list")
parser.add_argument('-o', '--out', help='Custom output dataset name')
parser.add_argument('-s', '--seed', type=int,
                    help='Random generator seed.', default=1984)
parser.add_argument('--min_list_length', type=int,
                    help='Minimal list length to be used in input data generation. Default: 2', default=2)
parser.add_argument('--max_list_length', type=int,
                    help='Maximum list length to be used in input data generation. Default: 5', default=5)
parser.add_argument('--examples_per_task', type=int,
                    help='Number of input-output tuples per task in training data. Defaults to 30. Default: 30', default=30)
parser.add_argument('--data_size', type=int,
                    help='The size of the training dataset generated. Default: 500', default=500)
parser.add_argument('--tab_length', type=int,
                    help='Length of tabs in spaces in source code. Default: 4', default=4)

args = parser.parse_args()

OUTPUT_PATH = args.path
DATASET_NAME = args.out

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

p = Pipeline(args.datapath, args.seed, args.data_size,
             args.examples_per_task, args.min_list_length, args.max_list_length, args.tab_length)
tasks, language, vocab = p.generate_data_shuffled()

with open(train_data_path + "/tasks.json", "w") as outfile:
    json.dump(tasks, outfile)
with open(train_language_data_path + "/language.json", "w") as outfile:
    json.dump(language, outfile)
with open(train_language_data_path + "/vocab.json", "w") as outfile:
    json.dump(vocab, outfile)

p = Pipeline(args.datapath, args.seed+1, args.data_size,
             args.examples_per_task, args.min_list_length, args.max_list_length, args.tab_length)
tasks, language, vocab = p.generate_data_shuffled()

with open(test_data_path + "/tasks.json", "w") as outfile:
    json.dump(tasks, outfile)
with open(test_language_data_path + "/language.json", "w") as outfile:
    json.dump(language, outfile)
with open(test_language_data_path + "/vocab.json", "w") as outfile:
    json.dump(vocab, outfile)
