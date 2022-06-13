from flask import Flask, render_template
from utils import get_all_candidates, get_candidate_by_id, get_candidates_by_name, get_candidates_by_skill
app = Flask(__name__)


@app.route("/")
def main_page():
    candidates = get_all_candidates()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:id>")
def card_page(id):
    candidate: dict = get_candidate_by_id(id)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def page_search_by_name(candidate_name):
    candidate_name = candidate_name.lower()
    candidates: list[dict] = get_candidates_by_name(candidate_name)
    return render_template('search.html', name=candidate_name, count = len(candidates), candidates=candidates)


@app.route("/skill/<skill_name>")
def page_skills(skill_name):
    candidates: list[dict] = get_candidates_by_skill(skill_name)
    return render_template('skill.html', count=len(candidates), candidates=candidates, skill=skill_name)


app.run()