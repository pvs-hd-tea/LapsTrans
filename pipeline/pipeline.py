from inspect import getsource, getmembers, isfunction
import importlib.util
import sys
import random
import re
from token import COMMENT as TOKEN_TYPE_COMMENT
import tokenize

# Parameters
DATA_SIZE = 200
EXAMPLES_PER_TASK = 30
MIN_LIST_LENGTH = 2
MAX_LIST_LENGTH = 5
INT_DEFINITION_SPACE = range(100)
BOOL_DEFINITION_SPACE = [True, False]
NEWLINE_SYMBOL = "NEWLINE_SYMBOL"

# replace f_file with the name of .py file containing functions
class Pipeline:
    def __init__(self, location, seed=1984):
        print("Loading functions from {}".format(location))
        self.location = location

        spec = importlib.util.spec_from_file_location("functions", location)
        functions = importlib.util.module_from_spec(spec)
        sys.modules["functions"] = functions
        spec.loader.exec_module(functions)

        self.function_list = getmembers(functions, isfunction)

        random.seed(seed)
        self.task_names_iterators = {}

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
            comments_tokenized = []
            for each in token_objs:
                if each.exact_type == TOKEN_TYPE_COMMENT:
                    comment_string = each.string
                    comment_string.replace(",","")
                    comment_string.replace(".","")
                    comment_string.replace("\n","")
                    comment_string.replace("#","")
                    comments_tokenized.extend(comment_string.split(' '))
            unique_comments_tokenized = {each for each in comments_tokenized}
            
            # filter out comments:
            token_objs = filter(lambda token: token.exact_type != TOKEN_TYPE_COMMENT, token_objs)
            
            unique_token_names = {token.string for token in token_objs}
            return list(unique_token_names) + list(unique_comments_tokenized) + [NEWLINE_SYMBOL]

    type_def_to_sample = {
        "int": random_int,
        "list-of-int": random_list_int,
        "list-of-bool": random_list_bool,
    } 


    def generate_data_strict(self):
        examples_data = []
        language_data = {}
        vocab_data = set()

        for (function_name, function) in self.function_list:
            if function_name not in self.task_names_iterators.keys():
                self.task_names_iterators[function_name] = 0
            self.task_names_iterators[function_name] += 1
            source_code = getsource(function)
            type_comment = re.search(
                "(?:\\n\s+)\#\s(.+)(?:\s\-\>\s)(.+)\s\#", source_code
            )
            source_code = source_code.replace(type_comment.group(0), "")
            input_type_string = type_comment.group(1)
            output_type_string = type_comment.group(2)
            examples = []
            for _ in range(EXAMPLES_PER_TASK):
                input = self.type_def_to_sample[input_type_string]()
                output = function(input)
                examples.append({"i": input, "o": output})
            examples_data.append(
                {
                    "type": {"input": input_type_string, "output": output_type_string},
                    "name": function_name,
                    "examples": examples,
                }
            )
            language_data[function_name] = source_code

        vocab_data = Pipeline.generate_vocab(self.location)
        return examples_data, language_data, vocab_data



    def generate_data_shuffled(self):
        examples_data = []
        language_data = {}
        vocab_data = set()

        for _ in range(DATA_SIZE):
            (function_name, function) = random.choice(self.function_list)
            if function_name not in self.task_names_iterators.keys():
                self.task_names_iterators[function_name] = 0
            task_name = function_name + str(self.task_names_iterators[function_name])
            self.task_names_iterators[function_name] += 1
            source_code = getsource(function)
            type_comment = re.search(
                "(?:\\n\s+)\#\s(.+)(?:\s\-\>\s)(.+)\s\#", source_code
            )
            source_code = source_code.replace(type_comment.group(0), "")
            input_type_string = type_comment.group(1)
            output_type_string = type_comment.group(2)
            examples = []
            for _ in range(EXAMPLES_PER_TASK):
                input = self.type_def_to_sample[input_type_string]()
                output = function(input)
                examples.append({"i": input, "o": output})
            examples_data.append(
                {
                    "type": {"input": input_type_string, "output": output_type_string},
                    "name": task_name,
                    "examples": examples,
                }
            )
            language_data[task_name] = source_code

        for source_code in language_data.values():
            source_code = source_code.split(" ")
            for word in source_code:
                vocab_data.add(word)
        if "" in vocab_data:
            vocab_data.remove("")
        vocab_data = list(vocab_data)

        return examples_data, language_data, vocab_data
