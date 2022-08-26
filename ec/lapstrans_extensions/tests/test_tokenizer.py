from laps_augmentations.code_tokenizer import tokenize_codestring


def test_simple():
    s = "def increment(inp):\n    return [each + 1 for each in inp]\n"
    result = tokenize_codestring(s)
