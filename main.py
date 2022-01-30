from flask import Flask
from function import get_settings, get_candidate_by_id

settings = get_settings()

app = Flask(__name__)


@app.route('/')
def page_index():
    online = settings.get("online")
    if online:
        return "Приложение работает"
    else:
        return "Приложение не работает"


@app.route('/candidate/<int:x>')
def page_candidate(x):
    candidate = get_candidate_by_id(x)

    return f"""
           <h1>{candidate["name"]}</h1>
           <p>{candidate["position"]}</p>
           <img src="{candidate["picture"]}" width=200/>
           <p>{candidate["skills"]}</p>
           """


app.run()
