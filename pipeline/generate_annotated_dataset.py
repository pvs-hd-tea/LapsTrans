import json
import os
from templater import Template, Token
from pathlib import Path

DATASET_NAME = "list_20"

def extract_templates(file):
    result = []
    buffer = ''
    for line in file.readlines():
        if line.startswith('######'):
            result.append(buffer)
            buffer = ''
        else:
            buffer += line
    if not buffer == '':
        result.append(buffer)
    return result

with open('pipeline/tokens/variables_tokens.json') as json_file:
    variable_tokens = Token.dict_from_json(json_file)
with open('pipeline/tokens/function_name_tokens.json') as json_file:
    word_tokens = Token.dict_from_json(json_file)
with open('pipeline/tokens/primitives_tokens.json') as json_file:
    operation_tokens = Token.dict_from_json(json_file)

try:
    os.remove('pipeline/generated_functions.py')
except FileNotFoundError as e:
    ...

with (open('pipeline/templates.txt', 'r') as templates_file,
    open('pipeline/generated_functions.py', 'a') as functions_file):
    template_strings = extract_templates(templates_file)
    for string in template_strings:
        t = Template(string, var_token_library=variable_tokens, word_token_library=word_tokens, operation_token_library=operation_tokens)
        functions_file.write(t.render())

train_data_path = "data/tasks/" + DATASET_NAME + "/train"
train_language_data_path = "data/language/" + DATASET_NAME + "/train"
test_data_path = "data/tasks/" + DATASET_NAME + "/test"
test_language_data_path = "data/language/" + DATASET_NAME + "/test"
for path in [
    train_data_path,
    train_language_data_path,
    test_data_path,
    test_language_data_path,
]:
    Path(path).mkdir(parents=True, exist_ok=True)

from pipeline import generate_data

train_data, train_language, train_vocab = generate_data()
with open(train_data_path + "/tasks.json", "w") as outfile:
    json.dump(train_data, outfile)
with open(train_language_data_path + "/language.json", "w") as outfile:
    json.dump(train_language, outfile)
with open(train_language_data_path + "/vocab.json", "w") as outfile:
    json.dump(train_vocab, outfile)

test_data, test_language, test_vocab = generate_data()
with open(test_data_path + "/tasks.json", "w") as outfile:
    json.dump(test_data, outfile)
with open(test_language_data_path + "/language.json", "w") as outfile:
    json.dump(test_language, outfile)
with open(test_language_data_path + "/vocab.json", "w") as outfile:
    json.dump(test_vocab, outfile)