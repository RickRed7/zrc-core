def calculate_utility_score(energy_in, compute_out, state_finality):
    """
    Calculates node weight based on the Sovereign Proof of Utility.
    """
    efficiency_coefficient = compute_out / energy_in
    finality_bonus = 1.2 if state_finality == "LOGIC_GATE_FINAL" else 1.0
    return (efficiency_coefficient * finality_bonus) ** 2

if __name__ == "__main__":
    # Test calculation for a standard node
    print(f"Utility Score: {calculate_utility_score(100, 85, 'LOGIC_GATE_FINAL')}")
