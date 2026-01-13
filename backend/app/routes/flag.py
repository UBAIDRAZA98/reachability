from fastapi import APIRouter, Cookie, HTTPException

router = APIRouter(prefix="/flag")

@router.get("")
def flag(compliance_auth: str | None = Cookie(default=None)):
    # Simple check - in a real CTF, use JWT or a signed secret
    if compliance_auth == "VALID_PROOF_SUBMITTED": 
        return {"flag": "Savvy{W1WJ_X_73CN0_F3$T}"}
    
    raise HTTPException(status_code=403, detail="Unauthorized: Compliance Proof Required")
