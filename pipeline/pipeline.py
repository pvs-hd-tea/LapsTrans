from inspect import getsource, getmembers, isfunction
import json
import random
from pathlib import Path
import re
import tokenize
from token import COMMENT as TOKEN_TYPE_COMMENT

# Parameters

# replace f_file with the name of .py file containing functions
import f_file as functions

FUNCTIONS_FILE = "f_file.py"
DATA_SIZE = 100
OUTPUT_FOLDER_NAME = "_list"
DATASET_NAME = f"list_{DATA_SIZE}"
EXAMPLES_PER_TASK = 30
SEED = 1984
MIN_LIST_LENGTH = 2
MAX_LIST_LENGTH = 9
INT_DEFINITION_SPACE = range(100)
BOOL_DEFINITION_SPACE = [True, False]

# Initialization

function_list = getmembers(functions, isfunction)

train_data_path = f"{OUTPUT_FOLDER_NAME}/tasks/{DATASET_NAME}/train"
train_language_data_path = f"{OUTPUT_FOLDER_NAME}/language/{DATASET_NAME}/train"
test_data_path = f"{OUTPUT_FOLDER_NAME}/tasks/{DATASET_NAME}/test"
test_language_data_path = f"{OUTPUT_FOLDER_NAME}/language/{DATASET_NAME}/test"
for path in [
    train_data_path,
    train_language_data_path,
    test_data_path,
    test_language_data_path,
]:
    Path(path).mkdir(parents=True, exist_ok=True)

random.seed(SEED)
task_names_iterators = {}

# Core


def random_list_int():
    list_len = random.randint(MIN_LIST_LENGTH, MAX_LIST_LENGTH)
    return random.choices(INT_DEFINITION_SPACE, k=list_len)


def random_list_bool():
    list_len = random.randint(MIN_LIST_LENGTH, MAX_LIST_LENGTH)
    return random.choices(BOOL_DEFINITION_SPACE, k=list_len)


def random_int():
    return random.choice(INT_DEFINITION_SPACE)

def generate_vocab(filename):
    with open(filename, 'rb') as byte_stream:
        token_objs = list(tokenize.tokenize(byte_stream.readline))
        # filter out comments:
        token_objs = filter(lambda token: token.exact_type != TOKEN_TYPE_COMMENT, token_objs)
        unique_token_names = {token.string for token in token_objs}
        return list(unique_token_names)


type_def_to_sample = {
    'int': random_int,
    'list-of-int': random_list_int,
    'list-of-bool': random_list_bool,
}

def generate_data():
    examples_data = []
    language_data = {}

    for _ in range(DATA_SIZE):
        (function_name, function) = random.choice(function_list)
        if function_name not in task_names_iterators.keys():
            task_names_iterators[function_name] = 0
        task_name = function_name + str(task_names_iterators[function_name])
        task_names_iterators[function_name] += 1
        source_code = getsource(function)
        type_comment = re.search(
            "(?:\\n\s+)\#\s(.+)(?:\s\-\>\s)(.+)\s\#", source_code)
        source_code = source_code.replace(type_comment.group(0), '')
        input_type_string = type_comment.group(1)
        output_type_string = type_comment.group(2)
        examples = []
        for _ in range(EXAMPLES_PER_TASK):
            input = type_def_to_sample[input_type_string]()
            output = function(input)
            examples.append({"i": input, "o": output})
        examples_data.append(
            {
                "type": {"input": input_type_string, "output": output_type_string},
                "name": task_name,
                "examples": examples,
            }
        )
        language_data[task_name] = [source_code]

    return examples_data, language_data


vocab = generate_vocab(f"pipeline/{FUNCTIONS_FILE}")
train_data, train_language = generate_data()

with open(train_data_path + "/tasks.json", "w") as outfile:
    json.dump(train_data, outfile)
with open(train_language_data_path + "/language.json", "w") as outfile:
    json.dump(train_language, outfile)
with open(train_language_data_path + "/vocab.json", "w") as outfile:
    json.dump(vocab, outfile)

test_data, test_language = generate_data()
with open(test_data_path + "/tasks.json", "w") as outfile:
    json.dump(test_data, outfile)
with open(test_language_data_path + "/language.json", "w") as outfile:
    json.dump(test_language, outfile)
with open(test_language_data_path + "/vocab.json", "w") as outfile:
    json.dump(vocab, outfile)
