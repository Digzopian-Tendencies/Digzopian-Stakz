from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_ecommerce_info():
    return {
        "module": "E-Commerce & Affiliate",
        "status": "active",
        "features": [
            "DIGZ token discount engine",
            "affiliate link generator",
            "dynamic merch pricing"
        ]
    }

@router.post("/discount")
def apply_discount(wallet: str, usd_price: float):
    discount = usd_price * 0.1
    return {
        "wallet": wallet,
        "original_price": usd_price,
        "discounted_price": usd_price - discount,
        "token_applied": True
    }
