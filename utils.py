import json


def load_candidates():
    """ Loads the full list of candidates """
    with open("candidates.json") as file:
        candidates_list = json.load(file)
    return candidates_list


def get_all_candidates() -> list[dict]:
    return load_candidates()




def get_candidate_by_id(id: int) -> dict | None:
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['id'] == id:
            return candidate
    return None


def get_candidates_by_name(name) -> list[dict]:
    result = []
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['name'].replace(" ", "").lower() == name:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill: str) -> list[dict]:
    result = []
    candidates = get_all_candidates()
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
