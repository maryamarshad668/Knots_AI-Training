# Day 2 

A simple propositional logic engine built from scratch in Python, used to solve two classic AI reasoning problems: the **Clue murder mystery** and **Knights & Knaves puzzles**.

## What this project does

Everything is built on one core idea: represent facts as logic sentences, then ask "does what I know **guarantee** that this other thing is true?" That question-answering is called **model checking** i.e trying every possible True/False combination and confirming the answer holds in all of them.

## Folder structure

```
day2_project/
├── logic.py         
├── model_check.py     
├── clue_solver.py      
└── puzzle.py          
```

## How to run

All four files should be in the **same folder**, then from that folder run:

```bash
python3 clue_solver.py
```
```bash
python3 puzzle.py
```

`logic.py` and `model_check.py` are not meant to be run directly 

## File-by-file explanation

### `logic.py`
Defines the classes that represent logical sentences:

| Class | Meaning | Example |
|---|---|---|
| `Symbol` | A basic fact | `Symbol("Rain")` |
| `Not` | Negation | `Not(rain)` → "it is not raining" |
| `And` | All must be true | `And(rain, cold)` |
| `Or` | At least one must be true | `Or(mustard, plum, scarlet)` |
| `Implication` | If-then | `Implication(rain, wet)` |
| `Biconditional` | Both sides match | `Biconditional(knight, statementIsTrue)` |


### `model_check.py`
Implements brute-force entailment checking: it tries every True/False combination for every symbol involved and confirms the query holds whenever the knowledge does. 

### `clue_solver.py`
Encodes the Clue board game as logic:
- At least one suspect is guilty, one weapon was used, one room is the scene
- Any card in your hand is marked `Not(card)` — since holding it proves it's innocent
- Extra hints revealed during play are added the same way

The solver then checks every suspect/weapon/room and reports one of three answers:
- **Definitely the answer** — proven guilty by the model checker
- **Definitely not the answer** — proven innocent
- **Unknown so far** — not enough information yet

### `puzzle.py`
Solves Knights & Knaves logic puzzles, where Knights always tell the truth and Knaves always lie. The key trick:

```
Biconditional(PersonIsKnight, WhatTheyClaimed)
```

This single line captures both rules at once. If the person is a Knight, their claim must be true. If a Knave, it must be false.

## Sample output

**Clue Solver:**
```
MsScarlet: definitely the answer
Library: definitely the answer
Candlestick: unknown so far
```

**Knights & Knaves:**
```
--- Puzzle 1 ---
No valid solution exists i.e the statements contradict themselves.

--- Puzzle 2 ---
A is Knave, B is Knight
```

## Concepts covered
- Propositional logic 
- Model checking 
- Knowledge engineering 
- Constraint satisfaction