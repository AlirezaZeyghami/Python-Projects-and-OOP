# PEP 8 & Formatting — Practical Guide

This note summarises the Python style guide (PEP 8), recommended formatting tools, and a few practical rules and examples you can use on your projects and push to your repo.

References:
- Official PEP 8: Python style guide. :contentReference[oaicite:0]{index=0}  
- Python style overview and history. :contentReference[oaicite:1]{index=1}  
- *Clean Code in Python* (recommended book for deeper habits). :contentReference[oaicite:2]{index=2}

---

## What is PEP 8 (short)
PEP 8 is the community style guide for Python code. It focuses on readability and consistency: indentation, line length, blank lines, import order, naming conventions, whitespace, and docstrings. Following PEP 8 makes your code easier to read and maintain. :contentReference[oaicite:3]{index=3}

---

## Quick, practical rules (the ones I follow)
- **Indentation:** 4 spaces per level (no tabs mixed with spaces).  
- **Maximum line length:** 79 characters for code (99 or 88 is commonly used by some formatters). Try to keep logical lines short.  
- **Blank lines:** separate top-level function and class definitions with two blank lines; methods inside classes with one blank line.  
- **Imports:** one per line; order them: standard library → third-party → local (use blank line between groups).  
- **Naming:**  
  - `snake_case` for functions and variables,  
  - `PascalCase` (CapWords) for classes,  
  - `UPPER_CASE` for constants,  
  - private attributes start with one underscore `_name`.  
- **Whitespace:** avoid extraneous spaces: e.g. `func(a, b)` not `func( a , b )`.  
- **Docstrings:** use triple quotes and PEP 257 conventions for modules, functions, classes.  
- **Avoid long inline comments** — prefer a short comment above a tricky block.

(These are condensed PEP 8 recommendations — see the official doc for exhaustive examples.) :contentReference[oaicite:4]{index=4}

---

## Example — Bad vs Good

**Bad:**
```python
def add( a,b ):
    return a+b
```
## Good:
```py
def add(a, b):
    """Return the sum of a and b."""
    return a + b
```
## Bad long line:
```py
result = some_function_with_many_params(1, 2, 3, 4, 5, 6, 7, 8)
```
## Better (wrap to multiple lines):
```py
result = some_function_with_many_params(
    1, 2, 3, 4,
    5, 6, 7, 8
)
```
## Tools that help (use one or combine)
Black — code formatter (opinionated)

Black automatically formats entire files to a consistent style (it’s intentionally opinionated). Use it to remove bikeshedding about spacing/line breaks. 

Install & run:
```
pip install black
black path/to/your_project
```
### Black prefers a line length of 88 by default (configurable in pyproject.toml). Example pyproject.toml:
```
[tool.black]
line-length = 88
target-version = ["py39"]
```
## Flake8 — linting / style enforcement

Flake8 checks style and simple errors (wraps pycodestyle, pyflakes, McCabe). Use it to detect unused imports, indentation issues, complexity, etc. 
flake8.pycqa.org

Install & run:
```
[flake8]
max-line-length = 88
ignore = E203, W503
exclude = .venv, build, dist
```
## Other useful tools

pylint — stricter linting and code-quality scoring (configurable).

isort — automatically sorts imports (can be integrated with Black).

editor integrations — many editors support Black/Flake8 directly (see below).

## Editor setup & quick shortcut

VS Code: your quick formatting shortcut is Shift + Alt + F (on Windows). Configure default formatter to Black in VS Code settings for automatic formatting on save:
```
"[python]": {
  "editor.defaultFormatter": "ms-python.black-formatter"
},
"editor.formatOnSave": true
```
(Replace with your chosen formatter extension.)
This makes formatting instant and consistent across your team.

## Recommended workflow (simple, practical)

Install formatter & linter in venv: pip install black flake8 isort.

Add pyproject.toml and/or .flake8 to project root.

Run black . to format.

Run flake8 . to catch remaining issues.

Add CI check: run black --check . and flake8 in your CI pipeline to enforce style on PRs.

## Why follow PEP 8 + a formatter?

PEP 8 gives conventions for readability; a formatter (Black) applies them consistently so reviewers can focus on logic, not style. The Clean Code in Python book is an excellent resource for deeper habits and refactor patterns.

## Quick references

PEP 8 — Style Guide for Python Code. 
Python Enhancement Proposals (PEPs)

Python style guide overview. 
Python.org

Black formatter docs. 
Black Documentation

Flake8 official site. 
flake8.pycqa.org

Clean Code in Python (book). 
oreilly.com
