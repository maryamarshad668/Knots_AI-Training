# Day 1 Project — Search Algorithms & Game AI

Two AI applications built using search algorithms and game trees.

## Folder Structure

Day1/
├── maze.py
├── mazes/
│ └── maze1.txt
├── tictactoe.py
└── runner.py


## 1. Maze Solver

Solves a maze using four different search algorithms and compares them.

**Algorithms implemented:**
- DFS (Stack Frontier)
- BFS (Queue Frontier)
- Greedy Best-First Search (Manhattan Heuristic)
- A* Search (Cost + Heuristic)

**Run it:**
```bash
python maze.py
```

**Output includes:**
- Start and goal coordinates
- Path found by each algorithm
- Comparison table of path length and states explored

## 2. Unbeatable Tic-Tac-Toe

An AI opponent that uses **Minimax** with **Alpha-Beta Pruning**. It never loses — best case for a human is a draw.

**Files:**
- `tictactoe.py` — game logic and AI (not run directly)
- `runner.py` — play the game against the AI

**Run it:**
```bash
python runner.py
```

**How to play:**
- AI is `X`, moves first
- You are `O`
- Enter moves as `row,col` using 0, 1, or 2

row,col: 1,2


## Concepts Covered

- Search Trees
- DFS / BFS
- Greedy Search / Heuristics
- A* Search / Priority Queue
- Game Trees
- Minimax
- Alpha-Beta Pruning
- Evaluation Functions