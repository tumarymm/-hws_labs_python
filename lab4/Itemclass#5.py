# 5
class Item:
    def __init__(self, item_id, name, power):
        self.id = item_id
        self.name = name
        self.power = power

    def __repr__(self):
        return f"{self.name}(id={self.id}, power={self.power})"


class Inventory:
    def __init__(self):
        self._items = []

    def add_item(self, item: Item):
        self._items.append(item)

    def get_strong_items(self, min_power: int):
        check_power = lambda item: item.power >= min_power

        return [item for item in self._items if check_power(item)]


inv = Inventory()
inv.add_item(Item(1, "Пышақ", 15))
inv.add_item(Item(2, "Қылыш", 55))
inv.add_item(Item(3, "Айбалта", 80))
inv.add_item(Item(4, "Қалқан", 20))

strong_stuff = inv.get_strong_items(50)

print("Мықты заттар (power >= 50):")
print(strong_stuff)