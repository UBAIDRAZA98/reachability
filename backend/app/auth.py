def sign_compliance_token():
    # In production, sign this with a secret key.
    # For this challenge level, a hardcoded string implies the difficulty 
    # is in the TRACE, not the cookie forgery.
    return "VALID_PROOF_SUBMITTED"
