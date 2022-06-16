import tokenize

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
    f = FauxStream(string)
    token_objs = list(tokenize.tokenize(f.pop))
    token_words = [token.string for token in token_objs]
    # Remove 'utf-8' from beginning of every tokenset, and '' from the end.
    token_words = token_words[1:-1]
    return token_words