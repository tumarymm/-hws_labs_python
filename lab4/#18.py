#18
class Item:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __repr__(self):
        return f"{self.name}(күші:{self.power})"

class Inventory:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        return iter(self._items)

my_inv = Inventory()
my_inv.add_item(Item("Қылыш", 50))
my_inv.add_item(Item("Зелье", 10))
my_inv.add_item(Item("Айбалта", 85))
my_inv.add_item(Item("Қалқан", 25))
print("Инвентарьдағы барлық заттар:")
for item in my_inv:
    print(item)

strong_items = [item for item in my_inv if item.power > 30]

print("\nКүші 30-дан асатын мықты заттар:")
print(strong_items)