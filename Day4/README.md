# Day 4 — CS50 AI: Optimization — CSP Mini Project

Three small solvers built around Constraint Satisfaction Problems (CSPs), backtracking search, and linear programming.

```
day4_project/
├── nqueens.py       # N-Queens as a CSP
├── crossword.py     # Crossword puzzle as a CSP
└── lp_scheduler.py  # Simple LP scheduler with PuLP
```

## Requirements

- Python 3.8+
- [PuLP](https://pypi.org/project/PuLP/) (only needed for `lp_scheduler.py`)

Install PuLP:

```
pip install pulp
```

---

## 1. `nqueens.py` — N-Queens Solver

Places N queens on an N×N board so that no two attack each other (same row, column, or diagonal).

**Approach**
- Variables: one per column (0 to N-1)
- Domain: row numbers (0 to N-1)
- Constraints: no shared row, no shared diagonal
- **AC-3** prunes impossible rows from each column's domain before search
- **Backtracking + MRV** picks the column with the fewest remaining options first

**Run it**

```
python nqueens.py
```

Change `n = 8` at the bottom of the file to solve a different board size.

**Example output**

```
Q . . . . . . .
. . . . . . Q .
. . . . Q . . .
. . . . . . . Q
. Q . . . . . .
. . . Q . . . .
. . . . . Q . .
. . Q . . . . .
```

---

## 2. `crossword.py` — Crossword Puzzle Solver

Fills a crossword grid with words from a given word list.

**Approach**
- Grid uses `.` for fillable cells and `#` for blocked cells
- Variables: each word slot, found by scanning the grid (`across`/`down`, start position, length)
- Domain: all dictionary words matching a slot's length
- Constraints: overlapping slots must agree on the shared letter; no word is reused
- **AC-3** removes words that could never match at an overlap
- **Backtracking + MRV** fills slots with the fewest valid words first

**Run it**

```
python crossword.py
```

Edit the `grid` and `words` list at the bottom of the file to try your own puzzle.

**Example output**

```
# c #
b a r
# t #
```

---

## 3. `lp_scheduler.py` — Shift Scheduler (Linear Programming)

Assigns workers to shifts at minimum total cost using PuLP.

**Approach**
- 3 shifts: `morning`, `afternoon`, `night`
- Binary variable `x[worker, shift]` = 1 if that worker is assigned that shift
- Constraint: each shift meets its minimum required headcount
- Constraint: each worker is assigned at most one shift
- Objective: minimize total cost across all assignments

**Run it**

```
python lp_scheduler.py
```

Edit `workers`, `cost`, or `min_required` at the top of the file to try other scenarios.

**Example output**

```
Status: Optimal
morning -> ['carol']
afternoon -> ['bob']
night -> ['dave']
Total cost = 66.0
```

---

## Concepts Covered

- Local search (hill climbing, simulated annealing)
- Constraint Satisfaction Problems (variables, domains, constraints)
- Arc consistency (AC-3)
- Backtracking search with MRV heuristic
- Linear programming with PuLP