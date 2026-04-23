#12
import random


def generate(players, items, n):
    events = []
    for player in players:
        for _ in range(n):
            event_type = (lambda: random.choice(["ATTACK", "HEAL", "LOOT"]))()
            events.append({
                "player": player["name"],
                "type": event_type,
                "item": random.choice(items) if event_type == "LOOT" else None,
                "damage": random.randint(5, 15) if event_type == "ATTACK" else 0,
                "heal": random.randint(5, 10) if event_type == "HEAL" else 0
            })
    return events


players = [{"name": "Тұмар"}, {"name": "Асыл"}]
items = ["Sword", "Shield", "Potion"]
events = generate(players, items, 3)
for e in events:
    print(e)