"""
test_harness.py  --  testing & evidence reference  --  Year 12 & 13

WHAT THIS DEMONSTRATES
    A tiny, reusable way to run a whole TABLE of test cases automatically and
    print a PASS/FAIL report. Copy the printed report straight into your
    assessment as testing evidence -- it shows expected, boundary AND invalid
    cases being checked in an organised way, which is what Merit and Excellence
    ask for.

    You do not need a testing library for this. A list of cases and a loop is
    enough, and it is clearer for a marker to read.

HOW TO RUN
    python test_harness.py
"""

# The function under test: work out a final price with an optional discount.
def final_price(price, discount_percent):
    if price < 0:
        raise ValueError("price cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount must be 0-100")
    return round(price * (1 - discount_percent / 100), 2)


# Each case: a description, the inputs, and what we EXPECT to happen.
# Use the string "ValueError" to mean "this input should be rejected".
TEST_CASES = [
    # description,                       price,  discount, expected
    ("expected: half price",            100.0,   50,       50.0),
    ("expected: no discount",            40.0,    0,        40.0),
    ("boundary: full discount",         100.0,  100,        0.0),
    ("boundary: zero price",              0.0,   25,        0.0),
    ("invalid: negative price",          -5.0,   10,       "ValueError"),
    ("invalid: discount over 100",       50.0,  150,       "ValueError"),
]


def run_tests(cases):
    passed = 0
    print(f"{'RESULT':<7}{'CASE':<32}{'GOT':>12}")
    print("-" * 51)
    for description, price, discount, expected in cases:
        try:
            got = final_price(price, discount)
        except ValueError:
            got = "ValueError"
        ok = (got == expected)
        passed += ok
        print(f"{'PASS' if ok else 'FAIL':<7}{description:<32}{str(got):>12}")
    print("-" * 51)
    print(f"{passed}/{len(cases)} passed")


def main():
    run_tests(TEST_CASES)


if __name__ == "__main__":
    main()
