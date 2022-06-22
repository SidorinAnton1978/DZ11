from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route("/")
def page_main():
    """ Главная страница"""
    candidates = load_candidates()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:id>")
def page_candidate(id):
    """Страница кандидата"""
    candidate = candidates_id(id)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def page_candidate_search(candidate_name):
    """Страница поиска кандидатов по имени"""
    candidates = candidates_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route("/skill/<skill>")
def page_skills_candidate(skill):
    """Страница поиска кандидатов по имени"""
    candidates = candidates_skills(skill)
    return render_template('skill.html', skill=skill, candidates=candidates)


if __name__ == '__main__':
    app.run(debug=True)
