from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_audio_info():
    return {
        "module": "Digz Audio",
        "status": "active",
        "features": [
            "cymatics pattern generator",
            "resonant frequency visualizer",
            "audio-to-geometry transformation"
        ]
    }

@router.post("/analyze")
def analyze_frequency(freq: float):
    return {"frequency": freq, "pattern_id": f"FRAC-{int(freq*3.6)}"}
