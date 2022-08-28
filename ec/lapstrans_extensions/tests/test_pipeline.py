from pipeline.pipeline import *


def test_soft_remove():
    d = [1, 2, 3, 4]
    soft_remove(d, 4)
    soft_remove(d, 5)
    assert d == [1, 2, 3]


def test_identity_mapping():
    identical = [
        {
            "i": [1, 2, 3],
            "o": [1, 2, 3],
        },
        {
            "i": [True, False],
            "o": [True, False],
        },
        {
            "i": 1,
            "o": 1,
        },
        {
            "i": True,
            "o": True
        },
    ]
    not_identical = [
        {
            "i": [1, 2, 3],
            "o": [1, 2, 3],
        },
        {
            "i": [True, False],
            "o": [True, False],
        },
        {
            "i": 1,
            "o": 1,
        },
        {
            "i": True,
            "o": False
        },
    ]
    almost0 = [
        {
            "i": [1, 2, 3],
            "o": [3, 2, 1],
        },
        {
            "i": [True, False],
            "o": [True, False],
        },
        {
            "i": 1,
            "o": 1,
        },
        {
            "i": True,
            "o": True
        },
    ]
    almost1 = [
        {
            "i": [1, 2, 3],
            "o": [1, 2, 3],
        },
        {
            "i": [True, False],
            "o": [True, True],
        },
        {
            "i": 1,
            "o": 1,
        },
        {
            "i": True,
            "o": True
        },
    ]
    assert is_identity_mapping(identical)
    assert not is_identity_mapping(not_identical)
    assert not is_identity_mapping(almost0)
    assert not is_identity_mapping(almost1)


def pipeline_bootstrap():
    p = Pipeline(
        input_path="tests/helpers/functions.py",
        data_size=4,
        examples_per_task=5,
        min_list_length=1,
        max_list_length=3,
        tab_length=4
    )
    return p


def test_pipeline_bootstrap():
    pipeline_bootstrap()


def test_random_list_int():
    p = pipeline_bootstrap()
    for _ in range(10):
        result = p._random_list_int()
        assert len(result) <= 3
        assert len(result) >= 1
        assert isinstance(result[0], int)


def test_random_list_bool():
    p = pipeline_bootstrap()
    for _ in range(10):
        result = p._random_list_bool()
        assert len(result) <= 3
        assert len(result) >= 1
        assert isinstance(result[0], bool)


def test_random_int():
    p = pipeline_bootstrap()
    for _ in range(10):
        result = p._random_int()
        assert isinstance(result, int)


def test_random_bool():
    p = pipeline_bootstrap()
    for _ in range(10):
        result = p._random_bool()
        assert isinstance(result, bool)


def test_generate_vocab():
    p = pipeline_bootstrap()
    vocab = p._generate_vocab()
    assert sorted(vocab) == sorted(
        ['m', '(', 'x', ':', ')', 'return', 'max', 'TAB_SYMBOL', 'NEWLINE_SYMBOL', 'def'])


def test_process_function():
    p = pipeline_bootstrap()

    def m(x):
        return max(x)
    examples, language = p.process_a_function(m.__name__, m)
    assert len(examples) == 2
    assert len(language) == 2
    integers = list(filter(lambda x: x['type']['input']
                           == 'list-of-int', examples))[0]
    booleans = list(filter(lambda x: x['type']['input']
                           == 'list-of-bool', examples))[0]
    assert list(language.keys()) == ['m00', 'm01']


def test_generate_data_strict():
    p = pipeline_bootstrap()
    examples, language, vocab = p.generate_data_strict()
    assert len(language) == 2


def test_generate_data_shuffled():
    p = pipeline_bootstrap()
    examples, language, vocab = p.generate_data_strict()
    assert len(examples[0]['examples']) == 5
    assert len(language) == 2


def test_identify_types():
    # Refer to the test_lapstrans_type_identification.py!
    pass
