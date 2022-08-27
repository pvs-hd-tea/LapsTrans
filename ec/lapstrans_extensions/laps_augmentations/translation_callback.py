import json
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from ec.dreamcoder.frontier import Frontier

WRITE_TO = "lapstrans_extensions/working_dir/translation.json"


def write_translations(frontiers: List[Frontier]) -> None:
    """When using LAPS to translate python code, this function will be called after one pass in dreamcoder.py, write down the translation results into .json file, and kill the execution.

    Args:
        frontiers (List[Frontier]): Results of the translation (returned from wakeGenerative() in dreamcoder.py)
    """
    translated = {}
    for frontier in frontiers:
        if len(frontier.entries) == 0:
            continue
        translated[frontier.task.name] = str(frontier.bestPosterior.program.body)
    with open(WRITE_TO, "w") as f:
        json.dump(translated, f)
    exit()