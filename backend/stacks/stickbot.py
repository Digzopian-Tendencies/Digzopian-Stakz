from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_stickbot_info():
    return {
        "module": "StickBot HRM Simulation",
        "status": "active",
        "features": [
            "reinforcement learning trainer",
            "multi-surface environments",
            "tool-based skill learning"
        ]
    }

@router.post("/train")
def train_stickbot(episodes: int = 1000):
    return {
        "episodes": episodes,
        "result": f"StickBot trained for {episodes} episodes (stub output)"
    }
