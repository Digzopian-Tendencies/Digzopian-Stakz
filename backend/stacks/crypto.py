from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_crypto_info():
    return {
        "module": "Digzopian Alpha Crypto",
        "status": "active",
        "features": [
            "flashloan arbitrage scanner",
            "Base & Optimism chain integration",
            "fraud watchdog module"
        ]
    }

@router.post("/scan")
def scan_opportunity(token: str):
    return {
        "token": token,
        "opportunity_found": True,
        "expected_profit_usd": 42.0,
        "chain": "Base"
    }
