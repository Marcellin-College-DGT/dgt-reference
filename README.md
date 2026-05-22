# Digital Technology references

A small library of references for NCEA Digital Technology, Year 12 & 13
(AS91896 at Level 2, AS91906 at Level 3). Published as one GitHub Pages site
with a landing page that links to each reference.

## What's here

```
index.html        landing page (links to each reference)
styles.css        ONE shared stylesheet, used by every page
tkinter/          the tkinter widget reference + its runnable demos
testing/          the testing & evidence reference + its runnable demos
```

- **tkinter/** — every widget needed for a Python GUI: what each is for, a
  complete runnable example, tk-vs-ttk notes, and a class-based capstone app.
- **testing/** — the testing, validation, and evidence that move a program from
  Achieved to Excellence: the three kinds of test case, input validation, a
  reusable test runner, and how to evidence it all.

Each reference's page links up to the shared `../styles.css`, so styling is
maintained in one place.

## Conventions across all references

- Every code example is a complete, runnable program.
- All file operations use `encoding="utf-8"` so te reo Māori macrons (ā ē ī ō ū)
  read and write correctly.
- Every demo runs under `if __name__ == "__main__":` via a `main()` function.

## Running the demos

tkinter ships with Python. Open a demo in VS Code with the Python extension and
press Run, or from a terminal, e.g.:

```
python tkinter/entry_demo.py
python testing/validation_demo.py
```

## Publishing with GitHub Pages

1. Push everything to the repository, keeping this folder layout (the root
   `index.html` must stay at the top level).
2. In the repo, go to **Settings → Pages**.
3. Under **Source**, choose **Deploy from a branch**, select `main` and `/ (root)`,
   then **Save**.
4. After a minute the site is live at `https://<your-username>.github.io/<repo-name>/`.
   The landing page links to `/tkinter/` and `/testing/`.

## One thing to update

The intro of each reference page has a placeholder repo link
(`github.com/your-school/dt-reference`). Swap it for your real repo URL once it
exists. All internal links (stylesheet and demo files) are relative and work as
soon as you push.
