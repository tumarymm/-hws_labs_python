#15
class Event:
    def __init__(self, type, data):
        self.type = type
        self.data = data

class Player:
    def __init__(self, player_id, name, hp):
        self.id = player_id
        self.name = name
        self._hp = hp
        self._inventory = []

    def handle_event(self, event):
        if event.type == "ATTACK":
            self._hp -= event.data
        elif event.type == "HEAL":
            self._hp += event.data
        elif event.type == "LOOT":
            self._inventory.append(event.data)

class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            reduced_damage = event.data * 0.9
            self._hp -= reduced_damage
            print(f"{self.name} (Warrior) 10% қорғаныс қолданды. Зиян: {reduced_damage}")
        else:
            super().handle_event(event)

class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            boosted_item = f"Improved {event.data} (+10% Power)"
            self._inventory.append(boosted_item)
            print(f"{self.name} (Mage) затты сиқырмен күшейтті: {boosted_item}")
        else:
            super().handle_event(event)


w = Warrior(1, "Тұмар", 100)
m = Mage(2, "Асыл", 80)


attack = Event("ATTACK", 50)
w.handle_event(attack)


loot = Event("LOOT", "Staff")
m.handle_event(loot)