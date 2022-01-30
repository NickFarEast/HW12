# -*- coding: utf-8 -*-
import json
from os.path import isfile
from flask import Flask, render_template

CANDIDATES_FILE_PATH = "candidates.json"
SETTINGS_FILE_PATH = "settings.json"


def get_candidates():
    if isfile(CANDIDATES_FILE_PATH):
        with open(CANDIDATES_FILE_PATH,encoding="utf-8") as file:
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


app = Flask(__name__)

candidates = get_candidates()
settings = get_settings()


@app.route('/')
def page_index():
    return render_template("index.html", **settings)


@app.route('/candidate/<int:x>')
def page_candidate(x):
    for candidate in candidates:
        if candidate.get("id") == x:
            return render_template("candidate.html", **candidate)


app.run()
