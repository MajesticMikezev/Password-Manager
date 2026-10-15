from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_vault():
    return {
        "message": "Vault API is working!"
    }