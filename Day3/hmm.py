transition = {
    "sun": {"sun": 0.8, "rain": 0.2},
    "rain": {"sun": 0.3, "rain": 0.7},
}
emission = {
    "sun": {"umbrella": 0.2, "no_umbrella": 0.8},
    "rain": {"umbrella": 0.9, "no_umbrella": 0.1},
}
initial = {"sun": 0.5, "rain": 0.5}
states = ["sun", "rain"]

def viterbi(observations):
    dp = [{}]
    back = [{}]
    for s in states:
        dp[0][s] = initial[s] * emission[s][observations[0]]
        back[0][s] = None
    for t in range(1, len(observations)):
        dp.append({})
        back.append({})
        for s in states:
            best_prob, best_prev = max(
                (dp[t-1][prev] * transition[prev][s] * emission[s][observations[t]], prev)
                for prev in states
            )
            dp[t][s] = best_prob
            back[t][s] = best_prev
    path = []
    last_state = max(states, key=lambda s: dp[-1][s])
    path.append(last_state)
    for t in range(len(observations) - 1, 0, -1):
        last_state = back[t][last_state]
        path.append(last_state)
    path.reverse()
    return path
obs = ["umbrella", "umbrella", "no_umbrella", "umbrella"]
print(viterbi(obs))