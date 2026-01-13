# filename: constraints.py

def invariant(state):
    # Sanity checks to prevent integer overflows or negative logic
    return (
        0 <= state.kyc_score <= 100
        and 0 <= state.risk_score <= 100
        and state.audit_depth >= 0
        and state.approvals >= 0
        and state.appeals >= 0
    )
