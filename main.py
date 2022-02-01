from flask import Flask, request,render_template
from function import get_settings, get_candidate_by_id, get_candidates, search_candidate_by_name, search_candidate_by_skill


app = Flask(__name__)


@app.route('/')
def page_index():
    settings = get_settings()
    return render_template("index.html", **settings)


@app.route('/candidate/<int:x>')
def page_candidate(x):
    candidate = get_candidate_by_id(x)

    return render_template("candidate.html", **candidate)


@app.route('/list/')
def page_list():
    candidates = get_candidates()
    return render_template("list.html", candidates=candidates)


@app.route('/search/')
def page_search_by_name():
    name = request.args.get("name", "")
    candidates = search_candidate_by_name(name)
    candidates_count = len(candidates)

    return render_template("search.html", candidates=candidates, candidates_count=candidates_count)


@app.route("/skill/<skill_name>")
def page_search_by_skill(skill_name):
    candidates = search_candidate_by_skill(skill_name)
    candidates_count = len(candidates)
    skill = skill_name

    return render_template("search.html", candidates=candidates, candidates_count=candidates_count, skill=skill)


app.run()
