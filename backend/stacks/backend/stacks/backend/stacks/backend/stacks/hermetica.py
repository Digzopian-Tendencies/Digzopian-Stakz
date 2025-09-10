from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_hermetica_info():
    return {
        "module": "Hermetic Codex",
        "status": "active",
        "features": [
            "Corpus Oculus",
            "Etapionis doctrine",
            "Sacred Recursion principle"
        ]
    }

@router.get("/sigil/{name}")
def get_sigil(name: str):
    return {"sigil": name, "meaning": f"Encoded hermetic symbol for {name}"}
