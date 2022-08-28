from utils.configuration import *
from pytest import raises


def test_base_parser():
    p = base_parser()
    args = [
        "--seed",
        "0",
        '--min_list_length',
        '1',
        '--max_list_length',
        '2',
        '--examples_per_task',
        '3',
        '--tab_length',
        '4'
    ]
    args = p.parse_args(args)
    assert args.seed == 0
    assert args.min_list_length == 1
    assert args.max_list_length == 2
    assert args.examples_per_task == 3
    assert args.tab_length == 4


def test_args_from_config_int():
    args = args_from_config(
        "tests/configurations/config_int.ini")
    assert isinstance(args.integer, int)


def test_args_from_config_str():
    args = args_from_config(
        "tests/configurations/config_string.ini")
    assert isinstance(args.string, str)


def test_args_from_config_bool():
    args = args_from_config(
        "tests/configurations/config_bool.ini")
    assert isinstance(args.yes, bool)
    assert args.yes
    assert not args.no


def test_args_from_config_section():
    args = args_from_config(
        "tests/configurations/config_section.ini", 'SUBSECTION')
    assert args.first
    assert args.second
    with raises(AttributeError):
        args.third


def test_translate_py_arguments():
    t = translate_py_arguments().parse_args(['--cli'])
    assert t.seed
    assert t.cli
    with raises(AttributeError):
        t.output_path


def test_generate_td_py_arguments():
    t = generate_td_py_arguments().parse_args([])
    assert t.output_path == './data/list'
    with raises(AttributeError):
        t.cli
