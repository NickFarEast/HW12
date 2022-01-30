# -*- coding: utf-8 -*-
import json
from os.path import isfile

CANDIDATES_FILE_PATH = "candidates.json"
SETTINGS_FILE_PATH = "settings.json"



def get_candidates():
    if isfile(CANDIDATES_FILE_PATH):
        with open(CANDIDATES_FILE_PATH, encoding="utf-8") as file:
            return json.load(file)
    else:
        print("Файл не найден")
        return {}


def get_settings():
    if isfile(SETTINGS_FILE_PATH):
        with open(SETTINGS_FILE_PATH) as file:
            return json.load(file)
    else:
        print("Файл не найден")
        return {}


def get_candidate_by_id(x):

    candidates = get_candidates()
    for candidate in candidates:
        if candidate.get("id") == x:
            return candidate

