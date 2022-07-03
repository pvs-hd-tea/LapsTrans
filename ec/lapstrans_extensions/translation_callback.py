import json

def write_translations(frontiers):
    translated = {}
    for frontier in frontiers:
        if len(frontier.entries) == 0:
            return None
        translated[frontier.task] = frontier.bestPosterior.program
    with open("translation.json", "w") as f:
        json.dump(translated, f)
    exit()