def calculate_utility_score(energy_in, compute_out, state_finality):
    efficiency = compute_out / energy_in
    bonus = 1.2 if state_finality == "LOGIC_GATE_FINAL" else 1.0
    return (efficiency * bonus) ** 2
