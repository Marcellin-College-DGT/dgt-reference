"""
cases_demo.py  --  testing & evidence reference  --  Year 12 & 13

WHAT THIS DEMONSTRATES
    The three kinds of test case the standards ask about, on ONE function:
        - expected  : ordinary, valid input the program is built for
        - boundary  : the values right on the edge of what is allowed
        - invalid   : input that should be rejected, not processed

    Knowing which case is which is what lets you say "I tested expected,
    boundary AND invalid cases" -- the line between Achieved, Merit, and
    Excellence on AS91896 (L2) and AS91906 (L3).

HOW TO RUN
    python cases_demo.py
"""

# The task: accept a class mark out of 100. Valid means a whole number 0-100.
LOWEST = 0
HIGHEST = 100


def grade_mark(mark):
    """Return a letter band for a mark, or raise ValueError if out of range."""
    if mark < LOWEST or mark > HIGHEST:
        raise ValueError(f"mark must be {LOWEST}-{HIGHEST}, got {mark}")
    if mark >= 80:
        return "Excellence"
    if mark >= 60:
        return "Merit"
    if mark >= 50:
        return "Achieved"
    return "Not Achieved"


def main():
    # EXPECTED cases -- ordinary valid marks from the middle of the range.
    expected = [55, 72, 90]

    # BOUNDARY cases -- the edges: lowest, highest, and the band thresholds.
    # Bugs hide here. Is 80 an Excellence? Is 0 allowed? Test the edges.
    boundary = [LOWEST, HIGHEST, 50, 60, 80]

    # INVALID cases -- values that must be REJECTED, not graded.
    invalid = [-1, 101, 150]

    print("EXPECTED cases (should all grade normally):")
    for mark in expected:
        print(f"  {mark:>4} -> {grade_mark(mark)}")

    print("\nBOUNDARY cases (check the edges behave exactly as intended):")
    for mark in boundary:
        print(f"  {mark:>4} -> {grade_mark(mark)}")

    print("\nINVALID cases (should be rejected with a clear message):")
    for mark in invalid:
        try:
            grade_mark(mark)
            print(f"  {mark:>4} -> NOT rejected  <-- this would be a bug")
        except ValueError as error:
            print(f"  {mark:>4} -> rejected: {error}")


if __name__ == "__main__":
    main()
