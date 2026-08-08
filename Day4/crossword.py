from collections import deque

def parse_variables(grid):
    variables = []
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == ".":
                if (c == 0 or grid[r][c-1] == "#") and (c+1 < cols and grid[r][c+1] == "."):
                    length = 0
                    cc = c
                    while cc < cols and grid[r][cc] == ".":
                        length += 1
                        cc += 1
                    variables.append((r, c, "across", length))
                if (r == 0 or grid[r-1][c] == "#") and (r+1 < rows and grid[r+1][c] == "."):
                    length = 0
                    rr = r
                    while rr < rows and grid[rr][c] == ".":
                        length += 1
                        rr += 1
                    variables.append((r, c, "down", length))
    return variables

def get_cells(var):
    r, c, d, l = var
    cells = []
    for i in range(l):
        if d == "across":
            cells.append((r, c+i))
        else:
            cells.append((r+i, c))
    return cells

def overlap(var1, var2):
    cells1 = get_cells(var1)
    cells2 = get_cells(var2)
    for i1, cell1 in enumerate(cells1):
        for i2, cell2 in enumerate(cells2):
            if cell1 == cell2:
                return (i1, i2)
    return None

def get_domains(variables, words):
    domains = {}
    for var in variables:
        length = var[3]
        domains[var] = [w for w in words if len(w) == length]
    return domains

def revise(domains, var1, var2):
    ov = overlap(var1, var2)
    if ov is None:
        return False
    i1, i2 = ov
    revised = False
    for w1 in domains[var1][:]:
        if not any(w1[i1] == w2[i2] for w2 in domains[var2]):
            domains[var1].remove(w1)
            revised = True
    return revised

def ac3(domains, variables):
    queue = deque()
    for v1 in variables:
        for v2 in variables:
            if v1 != v2 and overlap(v1, v2):
                queue.append((v1, v2))
    while queue:
        v1, v2 = queue.popleft()
        if revise(domains, v1, v2):
            if not domains[v1]:
                return False
            for v3 in variables:
                if v3 != v1 and v3 != v2 and overlap(v3, v1):
                    queue.append((v3, v1))
    return True

def consistent(assignment, var, word):
    if word in assignment.values():
        return False
    for v2, w2 in assignment.items():
        ov = overlap(var, v2)
        if ov:
            i1, i2 = ov
            if word[i1] != w2[i2]:
                return False
    return True

def select_unassigned(domains, assignment, variables):
    unassigned = [v for v in variables if v not in assignment]
    return min(unassigned, key=lambda v: len(domains[v]))

def backtrack(assignment, domains, variables):
    if len(assignment) == len(variables):
        return assignment
    var = select_unassigned(domains, assignment, variables)
    for word in domains[var]:
        if consistent(assignment, var, word):
            assignment[var] = word
            result = backtrack(assignment, domains, variables)
            if result is not None:
                return result
            del assignment[var]
    return None

def print_grid(grid, assignment):
    rows = len(grid)
    cols = len(grid[0])
    output = [["#" if grid[r][c] == "#" else "_" for c in range(cols)] for r in range(rows)]
    for var, word in assignment.items():
        cells = get_cells(var)
        for (r, c), letter in zip(cells, word):
            output[r][c] = letter
    for row in output:
        print(" ".join(row))

def solve(grid, words):
    variables = parse_variables(grid)
    domains = get_domains(variables, words)
    ac3(domains, variables)
    return backtrack({}, domains, variables)

if __name__ == "__main__":
    grid = [
        "#.#",
        "...",
        "#.#"
    ]
    words = ["cat", "bar", "dog", "ten"]
    solution = solve(grid, words)
    if solution:
        print_grid(grid, solution)
    else:
        print("no solution")