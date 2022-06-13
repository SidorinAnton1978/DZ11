class Candidate:
    def __init__(self, candidate_id: int, name: str, picture: str, position: str, skills: str):
        self.candidate_id = candidate_id
        self.name = name
        self.picture = picture
        self.position = position
        self.skills = skills

    def __repr__(self):
        return f"""Кандидат:\n{self.name}\n{self.picture}\n{self.position}\n{self.skills}"""
