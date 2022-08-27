import json

WRITE_TO = "lapstrans_extensions/working_dir/translation.json"

def write_translations(frontiers):
    translated = {}
    for frontier in frontiers:
        if len(frontier.entries) == 0:
            continue
        translated[frontier.task.name] = str(frontier.bestPosterior.program.body)
    with open(WRITE_TO, "w") as f:
        json.dump(translated, f)
    exit()