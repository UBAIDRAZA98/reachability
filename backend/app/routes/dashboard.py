from fastapi import APIRouter

router = APIRouter(prefix="/dashboard")

@router.get("")
def dashboard():
    return {
        "status": "ACTIVE",
        "compliance_score": 97,
        "workflow": "IN_PROGRESS"
    }
