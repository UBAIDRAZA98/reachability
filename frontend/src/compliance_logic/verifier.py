# filename: verifier.py
from state_machine import transition_allowed
from constraints import invariant

def verify_trace(states):
    # Must start at S0
    if not states or states[0].name != "S0":
        return False

    for i in range(len(states)):
        # 1. Check data integrity
        if not invariant(states[i]):
            return False
            
        # 2. Check transition from previous state
        if i > 0:
            if not transition_allowed(states[i - 1], states[i]):
                return False

    # Must reach the final state to get the flag
    return states[-1].name == "S6"
