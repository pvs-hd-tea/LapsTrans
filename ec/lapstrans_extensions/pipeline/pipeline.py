from inspect import getsource, getmembers, isfunction
import importlib.util
import sys
import random
import re
from token import COMMENT as TOKEN_TYPE_COMMENT
import tokenize
from typing import Dict, List, Tuple

# Parameters
INT_DEFINITION_SPACE = range(100)
BOOL_DEFINITION_SPACE = [True, False]
NEWLINE_SYMBOL = "NEWLINE_SYMBOL"

INT_TYPE = 'int'
BOOL_TYPE = 'bool'
INT_LIST_TYPE = 'list-of-int'
BOOL_LIST_TYPE = 'list-of-bool'
EMPTY_LIST = 'empty_list'


class Pipeline:
    """
    Handles generation of training data from a file path.
    Two functions you may be interested in are 
    generate_data_shuffled()
    and
    generate_data_strict()
    """

    def __init__(self, location, seed, data_size, examples_per_task, min_list_length, max_list_length):
        self.DATA_SIZE = data_size
        self.EXAMPLES_PER_TASK = examples_per_task
        self.MIN_LIST_LENGTH = min_list_length
        self.MAX_LIST_LENGTH = max_list_length
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
    def _random_list_int(self):
        list_len = random.randint(self.MIN_LIST_LENGTH, self.MAX_LIST_LENGTH)
        return random.choices(INT_DEFINITION_SPACE, k=list_len)

    def _random_list_bool(self):
        list_len = random.randint(self.MIN_LIST_LENGTH, self.MAX_LIST_LENGTH)
        return random.choices(BOOL_DEFINITION_SPACE, k=list_len)

    def _random_int(self):
        return random.choice(INT_DEFINITION_SPACE)

    def _random_bool(self):
        return random.choice(BOOL_DEFINITION_SPACE)

    def _generate_vocab(filename):
        """Generates vocabulary data for language model.

        Args:
            filename (str): File from which we extracted all the functions

        Returns:
            List: Vocabulary data.
        """
        with open(filename, 'rb') as byte_stream:
            token_objs = list(tokenize.tokenize(byte_stream.readline))
            comments_tokenized = []
            for each in token_objs:
                if each.exact_type == TOKEN_TYPE_COMMENT:
                    comment_string = each.string
                    comment_string.replace(",", "")
                    comment_string.replace(".", "")
                    comment_string.replace("\n", NEWLINE_SYMBOL)
                    comment_string.replace("#", "")
                    comments_tokenized.extend(comment_string.split(' '))
            unique_comments_tokenized = {each for each in comments_tokenized}

            # filter out comments:
            token_objs = filter(lambda token: token.exact_type !=
                                TOKEN_TYPE_COMMENT, token_objs)

            unique_token_names = {token.string for token in token_objs}
        result = list(unique_token_names) + \
            list(unique_comments_tokenized) + [NEWLINE_SYMBOL]
        result = list(set(result))
        result.remove("")
        result.remove('utf-8')
        result.remove('\n')
        return result

    _type_def_to_sample = {
        INT_TYPE: _random_int,
        BOOL_TYPE: _random_bool,
        INT_LIST_TYPE: _random_list_int,
        BOOL_LIST_TYPE: _random_list_bool,
    }

    def process_a_function(self, function_name, function) -> Tuple[List[Dict], List[Dict]]:
        """Generates pseudo training data (one example set per function). To be used for translating functions.

        Returns:
            List, Dict, List: List of examples, language annotation for all examples, vocabulary data for language mode
        """
        if function_name not in self.task_names_iterators.keys():
            self.task_names_iterators[function_name] = -1
        self.task_names_iterators[function_name] += 1
        source_code = getsource(function)
        types = Pipeline.identify_types(function)
        type_iter = 0
        example_set = []
        language_set = {}
        for input_type, output_type in types:
            task_name = function_name + \
                str(self.task_names_iterators[function_name]) + str(type_iter)
            examples = []
            for _ in range(self.EXAMPLES_PER_TASK):
                input = self._type_def_to_sample[input_type](self)
                output = function(input)
                examples.append({"i": input, "o": output})
            example = {
                "type": {"input": input_type, "output": output_type},
                "name": task_name,
                "examples": examples,
            }
            example_set.append(example)
            language_set.update({task_name: source_code})
            type_iter += 1
        return example_set, language_set

    def generate_data_shuffled(self) -> Tuple[List, Dict, List]:
        """Generates training data up to the DATA_SIZE. To be used for training data generation.

        Returns:
            List, Dict, List: List of examples, language annotation for all examples, vocabulary data for language mode
        """
        examples_data = []
        language_data = {}

        while len(examples_data) < self.DATA_SIZE:
            (function_name, function) = random.choice(self.function_list)
            example_set, language_set = self.process_a_function(
                function_name, function)
            examples_data.extend(example_set)
            language_data.update(language_set)

        vocab_data = Pipeline._generate_vocab(self.location)
        return examples_data, language_data, vocab_data

    def generate_data_strict(self):
        examples_data = []
        language_data = {}

        for (function_name, function) in self.function_list:
            example_set, language_set = self.process_a_function(
                function_name, function)
            examples_data.extend(example_set)
            language_data.update(language_set)

        vocab_data = Pipeline._generate_vocab(self.location)
        return examples_data, language_data, vocab_data

    def _infer_instance_type(instance) -> str:
        """Infers the type of an instance, returns one of:

        Args:
            instance (Any): instance to infer type of

        Raises:
            NotImplementedError: If the instance of an unexpected type

        Returns:
            str: One of
                INT_TYPE
                BOOL_TYPE
                INT_LIST_TYPE
                BOOL_LIST_TYPE
                EMPTY_LIST
        """
        if isinstance(instance, bool):
            return BOOL_TYPE
        if isinstance(instance, int):
            return INT_TYPE
        if isinstance(instance, list):
            if len(instance) == 0:
                return EMPTY_LIST
            if isinstance(instance[0], bool):
                return BOOL_LIST_TYPE
            if isinstance(instance[0], int):
                return INT_LIST_TYPE
        raise NotImplementedError

    def identify_types(function) -> List[Tuple[str, str]]:
        """Returns a list of all input-output type combinations, that could be processed by the passed function

        Returns:
            List[Tuple[str, str]]: List of tuples of types of input-output pairs,
            Each is one of: 
            INT_TYPE
            BOOL_TYPE
            INT_LIST_TYPE
            BOOL_LIST_TYPE
            EMPTY_LIST
        """

        INTEGER = 5
        BOOL = True
        INTEGER_LIST = [3, 4, 5]
        BOOL_LIST = [False, True]

        types = {
            INT_TYPE: None,
            BOOL_TYPE: None,
            INT_LIST_TYPE: None,
            BOOL_LIST_TYPE: None
        }

        try:
            test_return = function(INTEGER)
            types[INT_TYPE] = Pipeline._infer_instance_type(test_return)
        except Exception:
            pass

        try:
            test_return = function(BOOL)
            types[BOOL_TYPE] = Pipeline._infer_instance_type(test_return)
        except Exception:
            pass

        try:
            test_return = function(INTEGER_LIST)
            types[INT_LIST_TYPE] = Pipeline._infer_instance_type(test_return)
        except Exception:
            pass

        try:
            test_return = function(BOOL_LIST)
            types[BOOL_LIST_TYPE] = Pipeline._infer_instance_type(test_return)
        except Exception:
            pass

        result = []
        for key, value in types.items():
            if value != None:
                result.append((key, value))

        return result
