# Testing & evidence reference

A companion to the tkinter widget reference, for Year 12 & 13 Digital Technology
ākonga. Where the tkinter guide shows how to *build* a program, this one covers
the testing, validation, and evidence that move a program from Achieved to
Excellence on AS91896 (Level 2) and AS91906 (Level 3).

## What's here

- `index.html` — the reference page ākonga read (publish this with GitHub Pages).
- `styles.css` — the styling. It must sit beside `index.html`; if the two are
  separated the page loads unstyled. (Same stylesheet as the tkinter resource,
  with a few extra components for the grade ladder and test tables.)
- Four runnable, commented demo programs:
  - `cases_demo.py` — expected, boundary, and invalid cases on one function.
  - `validation_demo.py` — the same task written fragile, then robust.
  - `test_harness.py` — a reusable automatic test runner that prints PASS/FAIL.
  - `refinement_demo.py` — one function taken from Achieved to Excellence.

### Layout of the guide

- **The idea** — the grade ladder read as a testing ladder; the three kinds of case.
- **Making it robust** — validating input, handling the invalid case, named
  constants instead of magic numbers.
- **Evidencing it** — the test table, an automatic test runner, showing a bug fixed.
- **Putting it together** — one task shown at Achieved and at Excellence.

## Conventions used throughout

Consistent with the tkinter resource:

- Every code example is a complete, runnable program.
- All file operations use `encoding="utf-8"` so te reo Māori macrons (ā ē ī ō ū)
  read and write correctly.
- Every demo runs under `if __name__ == "__main__":` via a `main()` function.
- These demos are console programs, so they print their output rather than opening
  a window — the testing logic is identical whether input comes from `input()` or
  a tkinter `Entry`.

## Running the demos

tkinter is not required for these — they are plain Python. Open one in VS Code with
the Python extension and press Run, or from a terminal:

```
python validation_demo.py
```

## Publishing the reference with GitHub Pages

1. Push these files to the repository (keep `index.html` in the root).
2. In the repo, go to **Settings → Pages**.
3. Under **Source**, choose **Deploy from a branch**, select `main` and `/ (root)`,
   then **Save**.
4. After a minute the site is live at `https://<your-username>.github.io/<repo-name>/`.

## One thing to update

The intro of `index.html` has a placeholder repo link
(`github.com/your-school/testing-evidence-reference`). Swap it for your real repo
URL once it exists. The demo links are relative, so they work as soon as you push.
