import tokenize
from token import COMMENT as TOKEN_TYPE_COMMENT
from typing import List
TAB_SYMBOL = "TAB_SYMBOL"
NEWLINE_SYMBOL = "NEWLINE_SYMBOL"



class FauxStream:
    """
    Python tokenize library, although very useful to us, has a purpose so specific, 
    that it only takes readline-like callable generator objects, and in python 3.7 only with byte returns.
    Instead of digging deeper into tokenize lib, we make a fake bytestream-like wrapper.
    """

    def __init__(self, initial_content: str) -> None:
        """
        Args:
            initial_content (str): The content that this buffer will stream.
        """
        self.content = bytes(initial_content, 'utf-8')

    def pop(self) -> bytes:
        """The streaming callback

        Raises:
            StopIteration: raised once the buffer is empty

        Returns:
            bytes: Content of the buffer
        """
        if not self.content:
            raise StopIteration
        tmp = self.content
        self.content = None
        return tmp


def tokenize_codestring(string) -> List[str]:
    """Custom tokenizer for python source code. Since NLTK and other natural language tokenizers are useless in the context of reading source code, we replaced the tokenizer in LAPS dreamcoder with this one.
    
    Args:
        string (str): Python code in the utf-8 format. 

    Returns:
        List[str]: tokenized code
    
    """
    string = string.replace("\n", f" {NEWLINE_SYMBOL}")
    string = string.replace("\t", f" {TAB_SYMBOL} ")
    f = FauxStream(string)
    token_objs = list(tokenize.tokenize(f.pop))

    token_strings = []
    for each in token_objs:
        # The second token type is to filter out multiline """ comments """
        # might have sideeffects of removing actual strings
        # should not matter for list domain
        if each.exact_type == TOKEN_TYPE_COMMENT:
            comment_string = each.string
            comment_string.replace(",", "")
            comment_string.replace(".", "")
            comment_string.replace("#", "")
            token_strings.extend(comment_string.split(' '))
        else:
            token_strings.append(each.string)

    # Remove 'utf-8' from beginning of every tokenset,
    token_strings = token_strings[1:]
    while "" in token_strings:
        token_strings.remove("")
    return token_strings
