# 7
class Event:
    def __init__(self, type, data):
        self.type = type
        self.data = data


class Player:
    def __init__(self, id, name, hp):
        self.id = id
        self.name = name
        self._hp = hp
        self._inventory = []

    @property
    def hp(self):
        return self._hp

    @property
    def inventory(self):
        return self._inventory

    def handle_event(self, event):
        if event.type == "ATTACK":
            self._hp -= event.data
            print(f"{self.name} : зиян алды {event.data}. Қалған hp: {self._hp}")
        elif event.type == "HEAL":
            self._hp += event.data
            print(f"{self.name}: ем алды {event.data}. Қалған hp: {self._hp}")
        elif event.type == "LOOT":
            self._inventory.append(event.data)
            print(f"{self.name} : зат алды {event.data}")


class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            r = int(event.data) * 0.9
            self._hp -= r
            print(f"{self.name}(Warrior) зиян алды {r}, қалған hp {self._hp}")
        else:
            super().handle_event(event)


class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            b = f"{event.data} (+10% күш)"
            self._inventory.append(b)
            print(f"{self.name}(Mage) зат алды {b}")
        else:
            super().handle_event(event)


w = Warrior(1, "Тұмар", 100)
m = Mage(2, "Асыл", 80)

e1 = Event("ATTACK", 50)
e2 = Event("HEAL", 20)
e3 = Event("LOOT", "Қылыш")

w.handle_event(e1)
w.handle_event(e2)
m.handle_event(e3)
