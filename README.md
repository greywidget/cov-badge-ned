# cov-badge-ned
Simple example of a making a coverage badge based on Ned Batchelder's blog post

### Notes to self:
- Use `python -m pytest` (or `python -m pytest --cov`) to run tests. Just running `pytest` will cause import issues. I think this is because it's not a package.
- There are arguments for and against including test files in your coverage. I excluded them by adding the following to my `tox.ini`:
```
[coverage:run]
omit =
    */tests/*
```
