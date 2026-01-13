from backend.app.state_machine import transition_allowed
from backend.app.constraints import invariant

def verify_trace(states):
    if states[0].name != "S0":
        return False

    for i in range(len(states)):
        if not invariant(states[i]):
            return False
        if i > 0:
            if not transition_allowed(states[i - 1], states[i]):
                return False

    return states[-1].name == "S6"
