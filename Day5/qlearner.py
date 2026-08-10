import random

GRID = [
    [0, 0, 0, 0, 0],
    [0, -1, -1, 0, 0],
    [0, 0, 0, -1, 0],
    [0, -1, 0, 0, 0],
    [0, 0, 0, 0, "G"]
]

ROWS = len(GRID)
COLS = len(GRID[0])
START = (0, 0)
GOAL = (4, 4)
ACTIONS = ["up", "down", "left", "right"]

def is_wall(pos):
    r, c = pos
    return GRID[r][c] == -1

def in_bounds(pos):
    r, c = pos
    return 0 <= r < ROWS and 0 <= c < COLS

def move(pos, action):
    r, c = pos
    if action == "up":
        r -= 1
    elif action == "down":
        r += 1
    elif action == "left":
        c -= 1
    elif action == "right":
        c += 1
    return (r, c)

def reset():
    return START

def actions(state):
    return ACTIONS

def step(state, action):
    next_state = move(state, action)
    if not in_bounds(next_state) or is_wall(next_state):
        return state, -10, False
    if next_state == GOAL:
        return next_state, 100, True
    return next_state, -1, False

class QLearner:
    def __init__(self, alpha=0.5, epsilon=0.1, gamma=0.9):
        self.Q = {}
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma

    def get_q(self, state, action):
        return self.Q.get((state, action), 0)

    def choose_action(self, state, actions):
        if random.random() < self.epsilon:
            return random.choice(actions)
        return max(actions, key=lambda a: self.get_q(state, a))

    def update(self, state, action, reward, next_state, next_actions):
        best_next = max((self.get_q(next_state, a) for a in next_actions), default=0)
        old_q = self.get_q(state, action)
        new_q = old_q + self.alpha * (reward + self.gamma * best_next - old_q)
        self.Q[(state, action)] = new_q

agent = QLearner()

for episode in range(10000):
    state = reset()
    done = False
    steps = 0
    while not done and steps < 100:
        acts = actions(state)
        action = agent.choose_action(state, acts)
        next_state, reward, done = step(state, action)
        agent.update(state, action, reward, next_state, actions(next_state))
        state = next_state
        steps += 1

state = reset()
path = [state]
steps = 0
while state != GOAL and steps < 50:
    acts = actions(state)
    action = max(acts, key=lambda a: agent.get_q(state, a))
    state, reward, done = step(state, action)
    path.append(state)
    steps += 1

print("optimal path from start to goal:")
for p in path:
    print(p)