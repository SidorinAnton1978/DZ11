from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def page_main():
    """ Главная страница"""
    all_candidates: str = Candidate.format_candidate()
    return all_candidates


if __name__ == '__main__':
    app.run(debug=True)
