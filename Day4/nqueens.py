from collections import deque
import random

def get_domains(n):
    domains = {}
    for col in range(n):
        domains[col] = list(range(n))
    return domains

def conflict(r1, c1, r2, c2):
    return r1 == r2 or abs(r1 - r2) == abs(c1 - c2)

def neighbors(n, col):
    return [c for c in range(n) if c != col]

def revise(domains, n, xi, xj):
    revised = False
    for r1 in domains[xi][:]:
        if not any(not conflict(r1, xi, r2, xj) for r2 in domains[xj]):
            domains[xi].remove(r1)
            revised = True
    return revised

def ac3(domains, n):
    queue = deque()
    for xi in range(n):
        for xj in neighbors(n, xi):
            queue.append((xi, xj))
    while queue:
        xi, xj = queue.popleft()
        if revise(domains, n, xi, xj):
            if not domains[xi]:
                return False
            for xk in neighbors(n, xi):
                if xk != xj:
                    queue.append((xk, xi))
    return True

def select_unassigned(domains, assignment, n):
    unassigned = [c for c in range(n) if c not in assignment]
    return min(unassigned, key=lambda c: len(domains[c]))

def consistent(col, row, assignment):
    for c2, r2 in assignment.items():
        if conflict(row, col, r2, c2):
            return False
    return True

def backtrack(assignment, domains, n):
    if len(assignment) == n:
        return assignment
    col = select_unassigned(domains, assignment, n)
    for row in domains[col]:
        if consistent(col, row, assignment):
            assignment[col] = row
            result = backtrack(assignment, domains, n)
            if result is not None:
                return result
            del assignment[col]
    return None

def print_board(assignment, n):
    for row in range(n):
        line = ""
        for col in range(n):
            if assignment[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)

def solve(n):
    domains = get_domains(n)
    ac3(domains, n)
    return backtrack({}, domains, n)

if __name__ == "__main__":
    n = 8
    solution = solve(n)
    if solution:
        print_board(solution, n)
    else:
        print("no solution")