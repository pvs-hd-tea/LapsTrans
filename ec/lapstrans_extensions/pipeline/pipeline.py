from inspect import getsource, getmembers, isfunction
import importlib.util
import sys
import random
import re
from token import COMMENT as TOKEN_TYPE_COMMENT
import tokenize
from typing import Any, Dict, List, Tuple

# Parameters
INT_DEFINITION_SPACE = range(-10, 10)
BOOL_DEFINITION_SPACE = [True, False]
NEWLINE_SYMBOL = "NEWLINE_SYMBOL"
TAB_SYMBOL = "TAB_SYMBOL"

INT_TYPE = 'int'
BOOL_TYPE = 'bool'
INT_LIST_TYPE = 'list-of-int'
BOOL_LIST_TYPE = 'list-of-bool'
EMPTY_LIST = 'empty_list'


def soft_remove(l: List, v: Any) -> None:
    """Attempts to remove a value from the list in place, but does not raise an exception if value is not there

    Args:
        l (List): muteable list
        v (Any): value to remove
    """
    try:
        l.remove(v)
    except ValueError:
        pass


def is_identity_mapping(examples: List[Dict[str, Any]]) -> bool:
    """Checks if "i" and "o" in ALL tuples in examples match

    Args:
        examples (List[Dict[str, Any]]): examples generated within Pipeline.process_a_function() in a dreamcoder's solved examples format

    Returns:
        bool
    """
    match = True
    for each in examples:
        match = match and (each["i"] == each["o"])
    return match


class Pipeline:
    """
    Handles generation of training data from a given file path.
    Two functions you may be interested in are 
    generate_data_shuffled()
    and
    generate_data_strict()
    """

    def __init__(self, input_path: str = None, seed: int = None, data_size: int = None, examples_per_task: int = None, min_list_length: int = None, max_list_length: int = None, tab_length: int = None) -> None:
        """
        Args:
            input_path (str): The path to the input file containing functions used to generated examples and language.
            seed (int, optional): Seed used in random number generator. Defaults to 1984.
            data_size (int): The size of the training dataset. Only required if using Pipeline to generate training data.
            examples_per_task (int): Number of examples (i.e. input-output tuples per each task).
            min_list_length (int): Minimum length of an input list in every example.
            max_list_length (int): Maximum length of an input list in every example.
            tab_length (int): The length of indentation (if, as per PEP8, spaces are used for indentation).

        Raises:
            ValueError: If required argument is missed.
        """
        if input_path is None:
            raise ValueError('Pipeline requires input file path')
        if examples_per_task is None:
            raise ValueError(
                'Number of examples per task is not set. Did you specify default value?')
        if min_list_length is None:
            raise ValueError(
                'Minimum list length for input is not set. Did you specify default value?')
        if max_list_length is None:
            raise ValueError(
                'Maximum list length for input is not set. Did you specify default value?')
        if seed is None:
            seed = 1984

        self.DATA_SIZE = data_size
        self.EXAMPLES_PER_TASK = examples_per_task
        self.MIN_LIST_LENGTH = min_list_length
        self.MAX_LIST_LENGTH = max_list_length
        self.TAB_LENGTH = tab_length
        print("Loading functions from {}".format(input_path))
        self.location = input_path

        spec = importlib.util.spec_from_file_location("functions", input_path)
        functions = importlib.util.module_from_spec(spec)
        sys.modules["functions"] = functions
        spec.loader.exec_module(functions)

        self.function_list = getmembers(functions, isfunction)

        random.seed(seed)
        self.task_names_iterators = {}

    # Core
    def _random_list_int(self) -> List[int]:
        """List of random integers.

        Returns:
            List[int]
        """
        list_len = random.randint(self.MIN_LIST_LENGTH, self.MAX_LIST_LENGTH)
        return random.choices(INT_DEFINITION_SPACE, k=list_len)

    def _random_list_bool(self) -> List[bool]:
        """List of random booleans.

        Returns:
            List[bool]
        """
        list_len = random.randint(self.MIN_LIST_LENGTH, self.MAX_LIST_LENGTH)
        return random.choices(BOOL_DEFINITION_SPACE, k=list_len)

    def _random_int(self):
        return random.choice(INT_DEFINITION_SPACE)

    def _random_bool(self):
        return random.choice(BOOL_DEFINITION_SPACE)

    def _generate_vocab(self):
        """Generates vocabulary data for language model.

        Returns:
            List: Vocabulary data.
        """
        with open(self.location, 'rb') as byte_stream:
            token_objs = list(tokenize.tokenize(byte_stream.readline))
            comments_tokenized = []
            for each in token_objs:
                if each.exact_type == TOKEN_TYPE_COMMENT:
                    comment_string = each.string
                    comment_string.replace(",", "")
                    comment_string.replace(".", "")
                    comment_string.replace("\n", NEWLINE_SYMBOL)
                    comment_string.replace("\t", TAB_SYMBOL)
                    comment_string.replace("#", "")
                    comments_tokenized.extend(comment_string.split(' '))
            unique_comments_tokenized = {each for each in comments_tokenized}

            # filter out comments:
            token_objs = filter(lambda token: token.exact_type !=
                                TOKEN_TYPE_COMMENT, token_objs)

            unique_token_names = {token.string for token in token_objs}
        result = list(unique_token_names) + \
            list(unique_comments_tokenized) + [NEWLINE_SYMBOL, TAB_SYMBOL]
        result = list(set(result))
        soft_remove(result, "")
        soft_remove(result, "utf-8")
        soft_remove(result, "\n")
        soft_remove(result, "\t")
        tab = ' ' * self.TAB_LENGTH
        for i in range(10):
            soft_remove(result, i*tab)
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
        source_code = source_code.replace(self.TAB_LENGTH * ' ', '\t')
        types = Pipeline.identify_types(function)
        type_iter = 0
        example_set = []
        language_set = {}
        for input_type, output_type in types:
            task_name = function_name + \
                str(self.task_names_iterators[function_name]) + str(type_iter)
            examples = []
            done = False
            while not done:
                for _ in range(self.EXAMPLES_PER_TASK):
                    input = self._type_def_to_sample[input_type](self)
                    output = function(input)
                    examples.append({"i": input, "o": output})
                if is_identity_mapping(examples):
                    # If it's identity mapping, but data type is boolean, probably we just unnecessary identified that the function can accept booleans
                    if input_type == BOOL_LIST_TYPE or input_type == BOOL_TYPE:
                        examples = None
                        done = True
                    # If it's identity mapping, but data type is not boolean, regenerate data
                    else:
                        done = False
                else:
                    done = True
            if not examples:
                continue
            processed_data_for_function = {
                "type": {"input": input_type, "output": output_type},
                "name": task_name,
                "examples": examples,
            }
            example_set.append(processed_data_for_function)
            language_set.update({task_name: [source_code]})
            type_iter += 1
        return example_set, language_set

    def generate_data_shuffled(self) -> Tuple[List, Dict, List]:
        """Generates training data up to the DATA_SIZE. To be used for training data generation.

        Returns:
            List, Dict, List: List of examples, language annotation for all examples, vocabulary data for language mode
        """
        if self.DATA_SIZE is None:
            raise ValueError(
                "Can not generate training data without specifying target size of it.")
        examples_data = []
        language_data = {}

        while len(examples_data) < self.DATA_SIZE:
            (function_name, function) = random.choice(self.function_list)
            example_set, language_set = self.process_a_function(
                function_name, function)
            examples_data.extend(example_set)
            language_data.update(language_set)

        vocab_data = self._generate_vocab()
        return examples_data, language_data, vocab_data

    def generate_data_strict(self):
        examples_data = []
        language_data = {}

        for (function_name, function) in self.function_list:
            example_set, language_set = self.process_a_function(
                function_name, function)
            examples_data.extend(example_set)
            language_data.update(language_set)

        vocab_data = self._generate_vocab()
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
                # return EMPTY_LIST
                raise NotImplementedError
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
