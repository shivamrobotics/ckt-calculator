"""
Heat Exchanger Circuit Distribution Tool
-----------------------------------------
Constraint-based circuit distribution solver
Supports:
- Even / Odd / Both parity
- Minimum hole per circuit
- Dummy hole adjustment
- Two-size (s, s+2) feasibility search
"""

from typing import List, Dict


def find_two_step_solutions(U: int, N: int, parity: str, min_hole: int):
    solutions = []

    max_base = U // N + 20

    for s in range(max(min_hole, 0), max_base + 1):

        if parity == "even" and s % 2 != 0:
            continue
        if parity == "odd" and s % 2 == 0:
            continue

        s2 = s + 2

        numerator = (s2 * N - U)
        if numerator % 2 != 0:
            continue

        x = numerator // 2
        y = N - x

        if x < 0 or y < 0:
            continue

        if s * x + s2 * y != U:
            continue

        solutions.append({
            "base": s,
            "count_s": x,
            "count_s2": y
        })

    # Uniform solution
    if U % N == 0:
        val = U // N
        if (
            (parity == "both") or
            (parity == "even" and val % 2 == 0) or
            (parity == "odd" and val % 2 == 1)
        ) and val >= min_hole:
            solutions.append({
                "base": val,
                "count_s": N,
                "count_s2": 0
            })

    return solutions


def calculate_distribution(v, h, N, dummy, parity, min_hole):

    total = v * h
    usable = total - dummy

    if usable < N * min_hole:
        raise ValueError("Not enough usable holes for minimum requirement.")

    if parity == "even" and usable % 2 != 0:
        raise ValueError("Usable holes odd — cannot distribute only even values.")

    if parity == "both":
        base = usable // N
        extra = usable % N
        parts = [base] * N
        for i in range(extra):
            parts[i] += 1
        return parts

    solutions = find_two_step_solutions(usable, N, parity, min_hole)

    if not solutions:
        raise ValueError("No feasible distribution found.")

    best = solutions[0]
    parts = (
        [best["base"]] * best["count_s"] +
        [best["base"] + 2] * best["count_s2"]
    )

    return parts


def summarize(parts: List[int], v, h, dummy):

    total = v * h
    usable = total - dummy

    print("\n--- RESULT SUMMARY ---")
    print(f"Total Holes: {total}")
    print(f"Dummy Holes: {dummy}")
    print(f"Usable Holes: {usable}")
    print(f"Total Circuits: {len(parts)}")

    distribution: Dict[int, int] = {}
    for p in parts:
        distribution[p] = distribution.get(p, 0) + 1

    print("\nDistribution:")
    for k in sorted(distribution.keys()):
        print(f"  {distribution[k]} circuits with {k} holes")

    print("\nPer Circuit List:")
    print(parts[:40], "..." if len(parts) > 40 else "")


if __name__ == "__main__":

    print("Heat Exchanger Circuit Distribution Tool\n")

    v = int(input("Vertical holes: "))
    h = int(input("Horizontal holes: "))
    N = int(input("Number of circuits: "))
    dummy = int(input("Dummy holes: "))
    parity = input("Parity (even/odd/both): ").lower()
    min_hole = int(input("Minimum holes per circuit: "))

    try:
        parts = calculate_distribution(v, h, N, dummy, parity, min_hole)
        summarize(parts, v, h, dummy)
    except Exception as e:
        print("Error:", e)
        