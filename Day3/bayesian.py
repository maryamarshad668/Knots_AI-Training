CPT_Fire = {"fire": 0.01, "nofire": 0.99}

CPT_Alarm = {
    "fire":   {"alarm": 0.95, "noalarm": 0.05},
    "nofire": {"alarm": 0.10, "noalarm": 0.90},
}
CPT_Smoke = {
    "fire":   {"smoke": 0.90, "nosmoke": 0.10},
    "nofire": {"smoke": 0.05, "nosmoke": 0.95},
}
def joint_probability(fire, alarm, smoke):
    p_fire = CPT_Fire[fire]
    p_alarm = CPT_Alarm[fire][alarm]
    p_smoke = CPT_Smoke[fire][smoke]
    return p_fire * p_alarm * p_smoke

def query(target_var, evidence):
    fires = ["fire", "nofire"]
    alarms = ["alarm", "noalarm"]
    smokes = ["smoke", "nosmoke"]

    results = {}
    for target_val in (fires if target_var == "fire" else alarms if target_var == "alarm" else smokes):
        total = 0
        for f in fires:
            for a in alarms:
                for s in smokes:
                    assignment = {"fire": f, "alarm": a, "smoke": s}
                    if assignment[target_var] != target_val:
                        continue
                    if all(assignment[k] == v for k, v in evidence.items()):
                        total += joint_probability(f, a, s)
        results[target_val] = total

    normalizer = sum(results.values())
    return {k: v / normalizer for k, v in results.items()}
print(query("fire", {"alarm": "alarm", "smoke": "smoke"}))