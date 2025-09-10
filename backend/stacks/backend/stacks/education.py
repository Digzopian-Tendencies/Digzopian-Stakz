from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_education_info():
    return {
        "module": "School Attendant",
        "status": "active",
        "features": [
            "flashcards",
            "pop quizzes",
            "initiate training modules"
        ]
    }

@router.post("/quiz")
def generate_quiz(topic: str):
    return {
        "topic": topic,
        "questions": [
            {"q": f"What is {topic} in Digzopian lore?", "a": "TBD"},
            {"q": f"Name one symbol tied to {topic}", "a": "TBD"}
        ]
    }
