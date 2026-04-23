# 13
def analyze(events):
    total_damage = sum(e["damage"] for e in events if e.get("type") == "ATTACK")

    damage_per_player = {}
    for e in events:
        if e.get("type") == "ATTACK":
            p_name = e["player"]
            damage_per_player[p_name] = damage_per_player.get(p_name, 0) + e["damage"]

    return {
        "total_damage": total_damage,
        "damage_per_player": damage_per_player
    }


logs = [
    {"player": "Тұмар", "type": "ATTACK", "damage": 10},
    {"player": "Аяжан", "type": "HEAL", "heal": 5},
    {"player": "Балжан", "type": "ATTACK", "damage": 7}
]

print(analyze(logs))