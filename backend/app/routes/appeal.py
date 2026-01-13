from fastapi import APIRouter, Response
from backend.app.models import State
from backend.app.verifier import verify_trace
from backend.app.auth import sign_compliance_token  # We will add this

router = APIRouter(prefix="/appeal")

@router.post("")
def submit_appeal(trace: list[State], response: Response):
    if verify_trace(trace):
        # The user proved reachability. Grant them the token.
        token = sign_compliance_token()
        response.set_cookie(key="compliance_auth", value=token)
        return {"result": "ACCEPTED", "status": "Compliance Verified"}
    
    return {"result": "REJECTED"}
