# -*- coding: utf-8 -*-
import json
from os.path import isfile

CANDIDATES_FILE_PATH = "candidates.json"
SETTINGS_FILE_PATH = "settings.json"


def get_candidates():
    """
    Функция для получения списка кандидатов из json-файла.
    :return: словари с информацией о  кандидатах
    """
    if isfile(CANDIDATES_FILE_PATH):
        with open(CANDIDATES_FILE_PATH, encoding="utf-8") as file:
            return json.load(file)
    else:
        print("Файл не найден")
        return {}


def get_settings():
    """
    Функция для получения словаря с настройками из json-файла.
    :return: словарь с настройками
    """
    if isfile(SETTINGS_FILE_PATH):
        with open(SETTINGS_FILE_PATH) as file:
            return json.load(file)
    else:
        print("Файл не найден")
        return {}


def get_candidate_by_id(x):
    """
    Функция для извлечения информации о кандидате согласно введенному номеру id.
    :param x: id кандидата
    :return: возвращает словарь с информацией о кандидате согласно id
    """
    candidates = get_candidates()
    for candidate in candidates:
        if candidate.get("id") == x:
            return candidate
