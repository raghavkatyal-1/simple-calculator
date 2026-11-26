# Merge Conflict Log

| Step | Command | Result |
|------|---------|--------|
| 1 | `git checkout -b feature/safe-division` | Added a zero check to `divide()` and changed the README status line |
| 2 | `git checkout main && git checkout -b feature/rounding` | Changed `divide()` to `round(a / b, 4)` and the same README line |
| 3 | `git checkout main && git merge --no-ff feature/safe-division` | Clean merge, pushed to GitHub |
| 4 | `git merge feature/rounding` | **CONFLICT** in `README.md` and `calculator.py` |
| 5 | `git status`, `git diff`, `git log --merge` | Found the two unmerged files and the two commits that clashed |
| 6 | Manual edit | Kept **both** changes: the zero check plus rounding; merged the README text |
| 7 | `python3 -m unittest -v` | All 7 tests pass |
| 8 | `git add` + `git commit` + `git push` | Merge commit `0388229` pushed to `main` |

Resolved `divide()`:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return round(a / b, 4)
```
