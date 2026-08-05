import heapq
with open("mazes/maze1.txt") as f:
    lines = f.read().splitlines()
grid = lines
start = None
goal = None
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == "A":
            start = (r, c)
        if char == "B":
            goal = (r, c)
print("start", start)
print("goal", goal)

def actions(position):
    row, col = position
    moves = [
        ("up", (row - 1, col)),
        ("down", (row + 1, col)),
        ("left", (row, col - 1)),
        ("right", (row, col + 1))
    ]
    result_list = []
    for direction, (new_row, new_col) in moves:
        if new_row < 0 or new_row >= len(grid):
            continue
        if new_col < 0 or new_col >= len(grid[new_row]):
            continue
        if grid[new_row][new_col] == "#":
            continue
        result_list.append((direction, (new_row, new_col)))
    return result_list

def result(state, action):
    return action[1]
def goal_test(state):
    return state == goal
def step_cost(state, action):
    return 1
def manhattan(state, goal):
    (x1, y1) = state
    (x2, y2) = goal
    return abs(x1 - x2) + abs(y1 - y2)

class Node:
    def __init__(self, state, parent, action, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

class StackFrontier:
    def __init__(self):
        self.frontier = []
    def add(self, node):
        self.frontier.append(node)
    def contains_state(self, state):
        return any(n.state == state for n in self.frontier)
    def empty(self):
        return len(self.frontier) == 0
    def remove(self):
        node = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return node

class QueueFrontier(StackFrontier):
    def remove(self):
        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node

class GreedyFrontier:
    def __init__(self, goal, heuristic):
        self.heap = []
        self.counter = 0
        self.goal = goal
        self.heuristic = heuristic
    def add(self, node):
        h = self.heuristic(node.state, self.goal)
        heapq.heappush(self.heap, (h, self.counter, node))
        self.counter += 1
    def remove(self):
        h, _, node = heapq.heappop(self.heap)
        return node
    def empty(self):
        return len(self.heap) == 0
    def contains_state(self, state):
        return any(n.state == state for _, _, n in self.heap)

class AStarFrontier(GreedyFrontier):
    def add(self, node):
        priority = node.cost + self.heuristic(node.state, self.goal)
        heapq.heappush(self.heap, (priority, self.counter, node))
        self.counter += 1
def search(start_state, frontier):
    frontier.add(Node(start_state, None, None))
    explored = set()
    while True:
        if frontier.empty():
            return None, explored
        node = frontier.remove()
        if goal_test(node.state):
            return build_path(node), explored
        explored.add(node.state)
        for action in actions(node.state):
            child_state = result(node.state, action)
            child = Node(child_state, node, action, node.cost + step_cost(node.state, action))
            if child.state not in explored and not frontier.contains_state(child.state):
                frontier.add(child)

def build_path(node):
    path = []
    while node.parent is not None:
        path.append(node.action)
        node = node.parent
    path.reverse()
    return path

dfs_path, dfs_explored = search(start, StackFrontier())
bfs_path, bfs_explored = search(start, QueueFrontier())
greedy_path, greedy_explored = search(start, GreedyFrontier(goal, manhattan))
astar_path, astar_explored = search(start, AStarFrontier(goal, manhattan))

print("DFS path", dfs_path)
print("BFS path", bfs_path)
print("Greedy path", greedy_path)
print("A* path", astar_path)
print("Algorithm    Path length   States explored")
print("DFS         ", len(dfs_path), "         ", len(dfs_explored))
print("BFS         ", len(bfs_path), "         ", len(bfs_explored))
print("Greedy      ", len(greedy_path), "         ", len(greedy_explored))
print("A*          ", len(astar_path), "         ", len(astar_explored))