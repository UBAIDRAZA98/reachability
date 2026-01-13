from fastapi import APIRouter

router = APIRouter(prefix="/workflow")

@router.get("")
def workflow():
    return {
        "states": [
            "REGISTERED",
            "VERIFIED",
            "ASSESSED",
            "APPROVED",
            "AUDITED"
        ]
    }
