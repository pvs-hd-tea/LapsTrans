from pipeline.pipeline import Pipeline
from pipeline.pipeline import BOOL_TYPE, BOOL_LIST_TYPE, INT_TYPE, INT_LIST_TYPE


def test_to_Bool():
    def f(x):
        return False
    types = Pipeline.identify_types(f)
    for input, output in types:
        assert output == BOOL_TYPE


def test_to_Int():
    def f(x):
        return 5
    types = Pipeline.identify_types(f)
    for input, output in types:
        assert output == INT_TYPE


def test_to_Int_but_not_Bool_0():
    def f(x):
        return 0
    types = Pipeline.identify_types(f)
    for input, output in types:
        assert output == INT_TYPE


def test_to_Int_but_not_Bool_1():
    def f(x):
        return 1
    types = Pipeline.identify_types(f)
    for input, output in types:
        assert output == INT_TYPE


def test_Ambiguous_Mult():
    def f(x):
        return x*2
    types = Pipeline.identify_types(f)
    output_types = [t[1] for t in types]
    assert INT_TYPE in output_types
    assert INT_LIST_TYPE in output_types
    assert BOOL_LIST_TYPE in output_types


def test_Only_Bool():
    def f(x):
        if isinstance(x, bool):
            return 1
        raise Exception
    types = Pipeline.identify_types(f)
    assert len(types) == 1
    assert types[0][0] == BOOL_TYPE


def test_Only_Int():
    def f(x):
        if not isinstance(x, bool):
            if isinstance(x, int):
                return 1
        raise Exception
    types = Pipeline.identify_types(f)
    assert len(types) == 1
    assert types[0][0] == INT_TYPE


def test_Only_Int_List():
    def f(x):
        if not isinstance(x, list):
            raise Exception
        for value in x:
            if isinstance(value, bool):
                raise Exception
            if not isinstance(value, int):
                raise Exception
        return 1
    types = Pipeline.identify_types(f)
    assert len(types) == 1
    assert types[0][0] == INT_LIST_TYPE


def test_Only_Bool_List():
    def f(x):
        if not isinstance(x, list):
            raise Exception
        for value in x:
            if not isinstance(value, bool):
                raise Exception
        return 1
    types = Pipeline.identify_types(f)
    assert len(types) == 1
    assert types[0][0] == BOOL_LIST_TYPE
