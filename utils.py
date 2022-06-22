import json


def load_candidates(encoding='utf-8') ->list[dict]:
    """ Чтение данных из файла"""
    with open('candidates.json', 'r', encoding=encoding) as f:
        candidates = json.load(f)
        return candidates


def candidates_id(candidate_id: int) -> dict:
    """ Поиск кандидатов по id"""
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate


def candidates_name(name: str) -> list[dict]:
    """ Поиск по имени кандидата"""
    candidates = load_candidates()
    result = []
    for candidate in candidates:
        if candidate["name"] == name:
            result.append(candidate)
    return result


def candidates_skills(skill: str) -> list[dict]:
    """ Поиск по навыкам кандидата"""
    candidates = load_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
