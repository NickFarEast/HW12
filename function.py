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


def search_candidate_by_name(name):
    """
    Функция для поиска кандидатов в списке по имени.
    :param name: Имя по которому ищем кандидата
    :return: Возвращаем список кандидатов с искомым именем
    """

    settings = get_settings()
    case_sensitive = settings["case-sensitive"]
    candidates = get_candidates()
    candidates_match = []

    for candidate in candidates:

        if name in candidate["name"]:
            candidates_match.append(candidate)
            continue

        if not case_sensitive:
            if name.lower() in candidate["name"].lower():
                candidates_match.append(candidate)

    return candidates_match

def search_candidate_by_skill(skill_name):
    """
    Функция для поиска кандидатов из списка по навыкам.
    :param skill_name: название навыка
    :return: возвращает список кандидатов с искомым навыком
    """
    settings = get_settings()
    limit = settings["limit"]
    candidates = get_candidates()
    candidates_match = []

    skill_name = skill_name.lower()

    for candidate in candidates:

        skills = candidate["skills"].lower().split(", ")

        if skill_name in skills:
            candidates_match.append(candidate)

    return candidates_match[:limit]
