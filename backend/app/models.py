from pydantic import BaseModel

class State(BaseModel):
    name: str
    kyc_score: int
    risk_score: int
    compliance_flags: int
    audit_depth: int
    approvals: int
    appeals: int
    epoch: int
