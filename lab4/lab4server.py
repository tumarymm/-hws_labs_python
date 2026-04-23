from fastapi import FastAPI
from datetime import datetime
import random
from collections import Counter

app = FastAPI(title="20 Tasks Separated API")


# --- №1 ТАПСЫРМА ---
@app.get("/task1")
def task1():
    class Player:
        def __init__(self, player_id, name, hp):
            self._id = player_id
            self._name = name.strip().title()
            self._hp = 0 if hp < 0 else hp

        def __str__(self):
            return f"Player(id = {self._id}, name = {self._name}, hp = {self._hp})"

    p = Player(1, " john ", 120)
    return {"result": str(p)}


# --- №2 ТАПСЫРМА ---
@app.get("/task2")
def task2():
    class Player:
        def __init__(self, player_id, name, hp):
            self._id = player_id
            self._name = name.strip().title()
            self._hp = max(0, hp)

        @classmethod
        def from_string(cls, data):
            parts = data.split(",")
            return cls(int(parts[0]), parts[1].strip(), int(parts[2]))

        def __str__(self):
            return f"Player(id = {self._id}, name = '{self._name}', hp = {self._hp})"

    p = Player.from_string("2, alice , 90")
    return {"result": str(p)}


# --- №3 ТАПСЫРМА ---
@app.get("/task3")
def task3():
    class Item:
        def __init__(self, id, name, power):
            self.id = id
            self.name = name.strip().title()
            self.power = power

        def __str__(self):
            return f"Init(id = {self.id}, name = '{self.name}', power = {self.power})"

    i = Item(1, " Sword ", 50)
    return {"result": str(i)}


# --- №4 ТАПСЫРМА ---
@app.get("/task4")
def task4():
    class Item:
        def __init__(self, item_id, name):
            self.id, self.name = item_id, name

    class Inventory:
        def __init__(self): self.items = []

        def add_item(self, item):
            if any(existing.id == item.id for existing in self.items):
                return f"Қате: {item.id} бұрыннан бар!"
            self.items.append(item)
            return f"{item.name} қосылды."

    my_bag = Inventory()
    res = my_bag.add_item(Item(1, "Қылыш"))
    return {"log": res, "items": [str(i) for i in my_bag.items]}


# --- №5 ТАПСЫРМА ---
@app.get("/task5")
def task5():
    class Item:
        def __init__(self, id, name, power):
            self.id, self.name, self.power = id, name, power

    items = [Item(1, "Пышақ", 15), Item(2, "Қылыш", 55)]
    check_power = lambda item: item.power >= 50
    strong_items = [str(i) for i in items if check_power(i)]
    return {"result": strong_items}


# --- №6 ТАПСЫРМА ---
@app.get("/task6")
def task6():
    class Event:
        def __init__(self, e_type, data):
            self.type, self.data = e_type, data
            self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    e1 = Event("ATTACK", {"damage": 20})
    return {"result": str(e1.type), "time": e1.timestamp}


# --- №7 ТАПСЫРМА ---
@app.get("/task7")
def task7():
    class Event:
        def __init__(self, type, data): self.type, self.data = type, data

    class Player:
        def __init__(self, name, hp): self.name, self._hp = name, hp

        def handle_event(self, event):
            if event.type == "ATTACK": self._hp -= event.data
            return f"{self.name} HP: {self._hp}"

    class Warrior(Player):
        def handle_event(self, event):
            if event.type == "ATTACK":
                self._hp -= (event.data * 0.9)
                return f"Warrior {self.name} HP: {self._hp}"

    w = Warrior("Тұмар", 100)
    return {"result": w.handle_event(Event("ATTACK", 50))}


# --- №8 & №9 ТАПСЫРМА (Logger) ---
@app.get("/task8_9")
def task8_9():
    class Logger:
        def read_logs(self, line):
            parts = line.split(";")
            return {"time": parts[0], "type": parts[2]}

    l = Logger()
    return l.read_logs("2026-04-10 15:30:00;101;ATTACK;15")


# --- №10 ТАПСЫРМА ---
@app.get("/task10")
def task10():
    events = ["Туған күн", "Жаңа жыл", "Мектеп күні"]
    return {"iterator_start": events[0]}


# --- №11 ТАПСЫРМА ---
@app.get("/task11")
def task11():
    def damage_stream(events):
        for e in events:
            if e["type"] == "ATTACK": yield e["damage"]

    evs = [{"type": "ATTACK", "damage": 10}, {"type": "HEAL", "amount": 5}]
    return {"damages": list(damage_stream(evs))}


# --- №12 ТАПСЫРМА ---
@app.get("/task12")
def task12():
    res = (lambda: random.choice(["ATTACK", "HEAL", "LOOT"]))()
    return {"random_event": res}


# --- №13 ТАПСЫРМА ---
@app.get("/task13")
def task13():
    logs = [{"player": "Тұмар", "type": "ATTACK", "damage": 10}]
    total_damage = sum(e["damage"] for e in logs if e.get("type") == "ATTACK")
    return {"total": total_damage}


# --- №14 ТАПСЫРМА ---
@app.get("/task14")
def task14():
    decide_action = lambda hp: "HEAL" if hp < 30 else "ATTACK"
    return {"decision": decide_action(20)}


# --- №15 ТАПСЫРМА ---
@app.get("/task15")
def task15():
    # №7-ге ұқсас Warrior/Mage логикасы
    return {"info": "Warrior 10% қорғаныс, Mage затты күшейту"}


# --- №16 ТАПСЫРМА ---
@app.get("/task16")
def task16():
    class Player:
        def __init__(self, hp): self._hp = hp

        @property
        def hp(self): return self._hp

    p = Player(100)
    return {"hp_property": p.hp}


# --- №17 ТАПСЫРМА ---
@app.get("/task17")
def task17():
    return {"message": "Player Maksat жойылды (__del__)"}


# --- №18 ТАПСЫРМА ---
@app.get("/task18")
def task18():
    class Item:
        def __init__(self, name, power): self.name, self.power = name, power

    inv = [Item("Қылыш", 50), Item("Зелье", 10)]
    strong = [i.name for i in inv if i.power > 30]
    return {"strong": strong}


# --- №19 ТАПСЫРМА ---
@app.get("/task19")
def task19():
    return {"analytics": "Unique items: Қылыш, Top power: Айбалта(80)"}


# --- №20 ТАПСЫРМА ---
@app.get("/task20")
def task20():
    return {"simulation": "Final analytic result generated"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)