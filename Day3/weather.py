import random

transitions = {
    "sunny": {"sunny": 0.7, "cloudy": 0.2, "rainy": 0.1},
    "cloudy": {"sunny": 0.3, "cloudy": 0.4, "rainy": 0.3},
    "rainy": {"sunny": 0.2, "cloudy": 0.3, "rainy": 0.5},
}
def sample(dist):
    r = random.random()
    cumulative = 0
    for value, prob in dist.items():
        cumulative += prob
        if r <= cumulative:
            return value

def simulate(start, days):
    state = start
    history = [state]
    for _ in range(days):
        state = sample(transitions[state])
        history.append(state)
    return history

def steady_state(T, iterations=1000):
    states = list(T.keys())
    dist = {s: 1/len(states) for s in states}
    for _ in range(iterations):
        new_dist = {s: 0 for s in states}
        for s in states:
            for t in states:
                new_dist[t] += dist[s] * T[s][t]
        dist = new_dist
    return dist

history = simulate("sunny", 1000)
counts = {"sunny": 0, "cloudy": 0, "rainy": 0}
for h in history:
    counts[h] += 1
total = len(history)
empirical = {k: v/total for k, v in counts.items()}

print("Empirical:", empirical)
print("Steady state:", steady_state(transitions))