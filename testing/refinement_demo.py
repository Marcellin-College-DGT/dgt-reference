"""
refinement_demo.py  --  testing & evidence reference  --  Year 12 & 13

WHAT THIS DEMONSTRATES
    ONE small task taken on the journey the standards describe:
        version 1 (Achieved)   -- it works on expected input. That is all.
        version 2 (Excellence) -- well-structured, flexible, and robust.

    Read the two side by side. The logic is the same; the difference is
    validation, named constants instead of "magic numbers", clear structure,
    and handling the invalid case. THAT difference is the grade difference.

HOW TO RUN
    python refinement_demo.py
"""


# ===========================================================================
# VERSION 1 -- "it works" (Achieved)
# Magic numbers, no validation, crashes on bad input.
# ===========================================================================
def postage_v1(weight):
    if weight < 500:
        return 5
    elif weight < 2000:
        return 10
    else:
        return 20


# ===========================================================================
# VERSION 2 -- flexible and robust (Excellence)
# Named constants, input validation, invalid case handled, clear structure.
# ===========================================================================
LIGHT_LIMIT_G = 500       # constants, not magic numbers buried in the code
MEDIUM_LIMIT_G = 2000
MAX_WEIGHT_G = 30000

LIGHT_COST = 5
MEDIUM_COST = 10
HEAVY_COST = 20


def postage_v2(weight):
    # Validate first: reject anything that is not a sensible weight.
    if not isinstance(weight, (int, float)):
        raise TypeError("weight must be a number")
    if weight <= 0 or weight > MAX_WEIGHT_G:
        raise ValueError(f"weight must be between 1 and {MAX_WEIGHT_G} grams")

    # Derived from named constants, so the price bands are easy to change.
    if weight < LIGHT_LIMIT_G:
        return LIGHT_COST
    if weight < MEDIUM_LIMIT_G:
        return MEDIUM_COST
    return HEAVY_COST


def main():
    print("VERSION 1 (Achieved) -- works on expected input only:")
    for weight in (300, 1500, 5000):
        print(f"  {weight:>6} g -> ${postage_v1(weight)}")
    print("  ...but postage_v1(-10) returns $5, and postage_v1('heavy') crashes.")

    print("\nVERSION 2 (Excellence) -- same bands, now robust:")
    for weight in (300, 1500, 5000, -10, 40000):
        try:
            print(f"  {weight:>6} g -> ${postage_v2(weight)}")
        except (ValueError, TypeError) as error:
            print(f"  {weight:>6} g -> rejected: {error}")


if __name__ == "__main__":
    main()
