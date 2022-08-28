from laps_augmentations.code_tokenizer import tokenize_codestring


def test_increment():
    s = "def increment(inp):\n\treturn [each + 1 for each in inp]\n"
    result = tokenize_codestring(s)
    assert len(result) == 19
    assert result == ['def', 'increment', '(', 'inp', ')', ':', 'NEWLINE_SYMBOL', 'TAB_SYMBOL', 'return', '[',
                      'each', '+', '1', 'for', 'each', 'in', 'inp', ']', 'NEWLINE_SYMBOL']


def test_multiple_breaks():
    s = "def count_ones(inp):\n\taccu = 0\nfor each in inp:\n\t\tif each == 1:\n\t\t\taccu += 1\n\treturn accu"
    result = tokenize_codestring(s)
    assert len(result) == 35
    assert result == ['def', 'count_ones', '(', 'inp', ')', ':', 'NEWLINE_SYMBOL', 'TAB_SYMBOL', 'accu', '=', '0', 'NEWLINE_SYMBOLfor', 'each', 'in', 'inp', ':', 'NEWLINE_SYMBOL', 'TAB_SYMBOL',
                      'TAB_SYMBOL', 'if', 'each', '==', '1', ':', 'NEWLINE_SYMBOL', 'TAB_SYMBOL', 'TAB_SYMBOL', 'TAB_SYMBOL', 'accu', '+=', '1', 'NEWLINE_SYMBOL', 'TAB_SYMBOL', 'return', 'accu']


def test_list_comprehension():
    s = "def half_even(inp):\n\treturn [x/2 if x % 2 == 0 else x for x in inp]"
    result = tokenize_codestring(s)
    assert len(result) == 26
    assert result == ['def', 'half_even', '(', 'inp', ')', ':', 'NEWLINE_SYMBOL', 'TAB_SYMBOL', 'return',
                      '[', 'x', '/', '2', 'if', 'x', '%', '2', '==', '0', 'else', 'x', 'for', 'x', 'in', 'inp', ']']
