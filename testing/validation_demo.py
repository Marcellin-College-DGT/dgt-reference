"""
validation_demo.py  --  testing & evidence reference  --  Year 12 & 13

WHAT THIS DEMONSTRATES
    The same task written twice: once FRAGILE, once ROBUST.

    A fragile program assumes the user always types sensible input. The moment
    they don't, it crashes or stores nonsense. A robust program checks input
    for validity and handles the invalid case gracefully -- which is exactly
    what "flexible and robust" means in the standards, and what separates an
    Excellence program from one that merely "works".

HOW TO RUN
    python validation_demo.py
"""


# ---------------------------------------------------------------------------
# FRAGILE -- no validation. Works on good input, breaks on anything else.
# ---------------------------------------------------------------------------
def fragile_age(raw):
    age = int(raw)          # crashes with ValueError if raw is "abc" or ""
    return f"Next year you will be {age + 1}"


# ---------------------------------------------------------------------------
# ROBUST -- validates type AND range, returns a clear message instead of crashing
# ---------------------------------------------------------------------------
MIN_AGE = 0
MAX_AGE = 130


def robust_age(raw):
    raw = raw.strip()
    if not raw.isdigit():                 # rejects "", "abc", "-5", "3.5"
        return "Please enter your age as a whole number."
    age = int(raw)
    if age < MIN_AGE or age > MAX_AGE:    # rejects out-of-range numbers
        return f"Age must be between {MIN_AGE} and {MAX_AGE}."
    return f"Next year you will be {age + 1}"


def main():
    test_inputs = ["17", "  25 ", "abc", "", "-5", "200"]

    print("FRAGILE version:")
    for raw in test_inputs:
        try:
            print(f"  {raw!r:>8} -> {fragile_age(raw)}")
        except Exception as error:        # noqa: BLE001 (showing the crash on purpose)
            print(f"  {raw!r:>8} -> CRASH: {type(error).__name__}")

    print("\nROBUST version (same inputs, no crashes):")
    for raw in test_inputs:
        print(f"  {raw!r:>8} -> {robust_age(raw)}")

    # NOTE: in a tkinter program the only change is where 'raw' comes from --
    # raw = entry.get() instead of a list. The validation logic is identical.


if __name__ == "__main__":
    main()
