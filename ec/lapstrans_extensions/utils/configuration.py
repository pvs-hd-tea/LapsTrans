
import argparse
import configparser


def generate_td_py_arguments() -> argparse.Namespace:
    """Callback to initialize configuration for generate_training_data.py script from command line, or config file.

    Returns:
        argparse.Namespace: namespace with arguments used for Pipeline parameters and other tweaking.
    """
    parser = base_parser(
        description='Generate training data for LapsTrans project.')
    config_path = parser.parse_known_args(args=["config"])[0].config
    if config_path:
        return args_from_config(config_path, 'TRAINING DATA')
    else:
        parser.add_argument(
            '-i', '--input_path', help='Path of the file with functions used for training', type=str)
        parser.add_argument('-p', '--output_path', help='Custom output path. Default: ./data/list/',
                            default="./data/list")
        parser.add_argument('-o', '--output_name',
                            help='Custom output dataset name')
        parser.add_argument('--data_size', type=int,
                            help='The size of the training dataset generated. Default: 500', default=500)
        return parser.parse_known_args()[0]


def translate_py_arguments() -> argparse.Namespace:
    """Callback to initialize configuration for translate.py script from command line, or config file.

    Returns:
        argparse.Namespace: namespace with arguments used for Pipeline parameters and other tweaking.
    """
    parser = base_parser(
        description='Translate python code into lisp using LAPS/Dreamcoder')
    config_path = parser.parse_known_args()[0].config
    if config_path:
        return args_from_config(config_path, 'TRANSLATE')
    else:
        parser.add_argument('--cli', action='store_true', default=False)
        parser.add_argument(
            '-i', '--input_path', help='Path of the file with functions to translate.', type=str)

        parser.add_argument('-c', '--checkpoint_path',
                            help='Path of the *.pickle file with trained model. Default: trained.pickle', type=str, default="smart.pickle")
        return parser.parse_known_args()[0]


def base_parser(description: str = None) -> argparse.ArgumentParser:
    """Base argument parser, for arguments used in both translate.py and generate_training_data.py scripts.

    Args:
        description (str, optional): Description of the script as returned by cli. Defaults to None.

    Returns:
        argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        '--config', type=str, help="Path to the configuration file. If this is stated, all other arguments will be ignored")
    parser.add_argument('--seed', type=int,
                        help='Random generator seed.', default=1984)
    parser.add_argument('--min_list_length', type=int,
                        help='Minimal list length to be used in input data generation. Default: 2', default=2)
    parser.add_argument('--max_list_length', type=int,
                        help='Maximum list length to be used in input data generation. Default: 5', default=5)
    parser.add_argument('--examples_per_task', type=int,
                        help='Number of input-output tuples per task in training data. Default: 30', default=30)
    parser.add_argument('--tab_length', type=int,
                        help='Length of tabs in spaces in source code. Default: 4', default=4)
    return parser


def args_from_config(config_path: str, section_name: str = None):
    """Loads parameters for scripts from a .ini file instead of command line.

    Args:
        config_path (str): Path to .ini configuration.
        section_name (str, optional): The name of the extra section to load from config. [GLOBAL] section is always loaded, but may be overriden by values from this argument.

    Returns:
        Namespace-like object mimicking argparse.Namespace
    """
    config = configparser.ConfigParser()
    config.read(config_path)

    class Storage:
        pass
    storage = Storage()
    for key in config['GLOBAL']:
        storage.__setattr__(key, config['GLOBAL'][key])
    if section_name:
        for key in config[section_name]:
            storage.__setattr__(key, config[section_name][key])
    for k, v in storage.__dict__.items():
        if v.isdigit():
            storage.__setattr__(k, int(v))
        if v == "True":
            storage.__setattr__(k, True)
        if v == "False":
            storage.__setattr__(k, False)
    return storage