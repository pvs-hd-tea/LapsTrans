import tokenize
from token import COMMENT as TOKEN_TYPE_COMMENT
NEWLINE_SYMBOL = "NEWLINE_SYMBOL"

class FauxStream:
    """
    Python tokenize library, although very useful to us, has a purpose so specific, 
    that it only takes readline-like callable generator objects, and in python 3.7 only with byte returns.
    Instead of digging deeper into tokenize lib, we make a fake bytestream-like wrapper.
    """
    def __init__(self, initial_content) -> None:
        self.content = bytes(initial_content, 'utf-8')

    def pop(self) -> bytes:
        if not self.content:
            raise StopIteration
        tmp = self.content
        self.content = None
        return tmp

def tokenize_codestring(string):
    string = string.replace("\n", f" {NEWLINE_SYMBOL}")
    f = FauxStream(string)
    token_objs = list(tokenize.tokenize(f.pop))

    token_strings = []
    for each in token_objs:
        # The second token type is to filter out multiline """ comments """
        # might have sideeffects of removing actual strings
        # should not matter for string domain
        if each.exact_type == TOKEN_TYPE_COMMENT:
            comment_string = each.string
            comment_string.replace(",","")
            comment_string.replace(".","")
            comment_string.replace("#","")
            token_strings.extend(comment_string.split(' '))
        else:
            token_strings.append(each.string)
    
    # Remove 'utf-8' from beginning of every tokenset, and '' from the end.
    return token_strings[1:-1]