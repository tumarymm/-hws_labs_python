# 20
import random
import json
from collections import Counter


class Event:
    def __init__(self, player_id, e_type, data):
        self.player_id = player_id
        self.type = e_type
        self.data = data


class Player:
    def __init__(self, p_id, name, hp):
        self.id = p_id
        self.name = name
        self._hp = hp
        self._inventory = []
        self.total_damage_received = 0

    def handle_event(self, event):
        if event.type == "ATTACK":
            self._hp -= event.data
            self.total_damage_received += event.data
        elif event.type == "HEAL":
            self._hp += event.data
        elif event.type == "LOOT":
            self._inventory.append(event.data)


def generate_random_events(players, items, count):
    types = ["ATTACK", "HEAL", "LOOT"]
    events = []
    for _ in range(count):
        p = random.choice(players)
        e_type = random.choice(types)
        if e_type == "ATTACK":
            data = random.randint(10, 40)
        elif e_type == "HEAL":
            data = random.randint(5, 20)
        else:
            data = random.choice(items)
        events.append(Event(p.id, e_type, data))
    return events


def main():
    print(" Ойын симуляциясы басталды...\n")

    players = [Player(1, "Тұмар", 100), Player(2, "Асыл", 100)]
    items = ["Алтын қылыш", "Сиқырлы таяқ", "Темір қалқан"]

    events = generate_random_events(players, items, 10)

    with open("final_game_logs.txt", "w", encoding="utf-8") as f:
        for e in events:

            log_entry = f"{e.player_id};{e.type};{e.data}\n"
            f.write(log_entry)

            for p in players:
                if p.id == e.player_id:
                    p.handle_event(e)

    print(" Барлық оқиғалар 'final_game_logs.txt' файлына жазылды.")

    top_damaged_player = max(players, key=lambda p: p.total_damage_received)

    top_looter = max(players, key=lambda p: len(p._inventory))

    event_counts = Counter([e.type for e in events])

    print("\n--- АНАЛИТИКА ҚОРЫТЫНДЫСЫ ---")
    print(f"Ең көп зақым алған: {top_damaged_player.name} ({top_damaged_player.total_damage_received} HP)")
    print(f" Ең көп заты бар: {top_looter.name} ({len(top_looter._inventory)} зат)")
    print(f"Оқиғалар саны: {dict(event_counts)}")
    print("\n Симуляция аяқталды.")

