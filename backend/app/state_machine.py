VALID_STATES = {
    "S0", "S1", "S2", "S3", "S4", "S5", "S6"
}

def transition_allowed(prev, curr):
    if curr.epoch <= prev.epoch:
        return False

    match (prev.name, curr.name):
        case ("S0", "S1"):
            return prev.epoch == 0
        case ("S1", "S2"):
            return curr.kyc_score >= 85
        case ("S2", "S3"):
            return curr.risk_score <= (100 - curr.kyc_score)
        case ("S3", "S4"):
            return curr.approvals >= 2 and curr.compliance_flags == 0
        case ("S4", "S5"):
            return curr.audit_depth < 3 and curr.appeals == 0
        case ("S5", "S6"):
            return (
                curr.audit_depth == curr.appeals + 1
                and curr.kyc_score + curr.risk_score == 100
            )
        case _:
            return False
