# Day 3 Project — Probabilistic AI Systems

## Files
- weather.py — Markov chain weather simulator
- bayesian.py — Bayesian network inference (Fire-Alarm-Smoke)
- hmm.py — Hidden Markov Model Viterbi decoder

---

## weather.py — Markov Chain

Simulates weather using a Markov chain with states sunny, cloudy, rainy.

- simulate(start, days) — generates a sequence of weather states
- steady_state(T) — finds long-run probabilities using power iteration
- Runs a 1000-day simulation and compares empirical frequencies to the steady state

Run:
```
python weather.py
```

---

## bayesian.py — Bayesian Network

Models the classic Fire → Alarm, Fire → Smoke Bayesian network.

- joint_probability(fire, alarm, smoke) — computes joint probability from CPTs
- query(target_var, evidence) — computes posterior probability using exact enumeration

Run:
```
python bayesian.py
```
Example output answers P(Fire | Alarm=alarm, Smoke=smoke).

---

## hmm.py — Hidden Markov Model

Implements the Viterbi algorithm to decode the most likely hidden weather sequence from umbrella observations.

- viterbi(observations) — returns most likely hidden state sequence

Run:
```
python hmm.py
```
Test input:
```
["umbrella", "umbrella", "no_umbrella", "umbrella"]
```

---

## The Common Thread

All three models answer the same underlying question — how do you reason under uncertainty when you can't observe everything directly — but each assumes a different structure:

- **Markov chains** — state is fully observable; only time-dependence matters
- **Bayesian networks** — variables are observable; the causal/dependency structure matters
- **HMMs** — state is hidden and evolves over time; only indirect evidence is observed

This is also roughly the order of complexity in which they're usually taught: each model adds a layer of uncertainty the previous one couldn't handle.

## Requirements
Python 3