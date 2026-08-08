import pulp

workers = ["alice", "bob", "carol", "dave"]
shifts = ["morning", "afternoon", "night"]
cost = {
    "alice": {"morning": 20, "afternoon": 25, "night": 40},
    "bob":   {"morning": 22, "afternoon": 20, "night": 35},
    "carol": {"morning": 18, "afternoon": 24, "night": 30},
    "dave":  {"morning": 25, "afternoon": 22, "night": 28}
}
min_required = {
    "morning": 1,
    "afternoon": 1,
    "night": 1
}
prob = pulp.LpProblem("shift_scheduling", pulp.LpMinimize)

x = {}
for w in workers:
    for s in shifts:
        x[(w, s)] = pulp.LpVariable(f"{w}_{s}", cat="Binary")

prob += pulp.lpSum(cost[w][s] * x[(w, s)] for w in workers for s in shifts)

for s in shifts:
    prob += pulp.lpSum(x[(w, s)] for w in workers) >= min_required[s]
for w in workers:
    prob += pulp.lpSum(x[(w, s)] for s in shifts) <= 1
prob.solve(pulp.PULP_CBC_CMD(msg=0))

print("Status:", pulp.LpStatus[prob.status])
for s in shifts:
    assigned = [w for w in workers if x[(w, s)].varValue == 1]
    print(s, "->", assigned)
print("Total cost =", pulp.value(prob.objective))