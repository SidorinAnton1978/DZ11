import json


class Candidate:
    def __init__(self, candidate_id: int, name: str, picture: str, position: str, gender: str, age: int, skills: str):
        self.candidate_id = candidate_id
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills

    def __repr__(self):
        return f"""Кандидат:\n{self.name}\n{self.picture}\n{self.position}\n{self.skills}"""

    def load_json(self, filename, encoding='utf-8'):
        """ Чтение данных из файла"""
        with open(filename, 'r', encoding=encoding) as f:
            return json.load(f)

    def load_candidates(self) -> list[dict]:
        """ Загружает кандидатов из файла candidates.json в список """
        candidates = self.load_json('candidates.json')
        return candidates

    def candidates_id(self, id: int) -> dict:
        """ Поиск кандидатов по id"""
        candidates = self.load_candidates()
        for candidate in candidates:
            if candidate['id'] == id:
                return candidate

    def candidates_skills(self, skill: str) -> list[dict]:
        """ Поиск по навыкам кандидата"""
        candidates = self.load_candidates()
        result = []
        for candidate in candidates:
            if skill in candidate['skills'].lower().split(', '):
                result.append(candidate)
        return result

    def candidates_picture(self, id: int) -> str:
        """ Поиск картинки(фото) кандидата"""
        candidates = self.load_candidates()
        for candidate in candidates:
            if candidate['id'] == id:
                picture = f'<img src="{candidate["picture"]}">'
                return picture

