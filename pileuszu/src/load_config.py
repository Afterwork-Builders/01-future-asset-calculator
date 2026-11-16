import json


def load_config(config_path):
    with config_path.open("r", encoding="utf-8") as file:
        return json.load(file)
