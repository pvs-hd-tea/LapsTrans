import json

WRITE_TO = "../pipeline/translation.json"

def write_translations(frontiers):
    translated = {}
    for frontier in frontiers:
        if len(frontier.entries) == 0:
            return None
        translated[frontier.task.name] = str(frontier.bestPosterior.program.body)
    with open(WRITE_TO, "w") as f:
        json.dump(translated, f)
    exit()