# 19
def analyze_inventory(inventories):
    all_items = []
    for inv in inventories:
        all_items.extend(list(inv))

    unique_names = {item.name for item in all_items}

    if all_items:

        top_item = max(all_items, key=lambda x: x.power)
    else:
        top_item = None

    return {
        "unique_items": unique_names,
        "top_power": top_item
    }


class Item:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __repr__(self):
        return f"{self.name}({self.power})"


inv1 = [Item("Қылыш", 50), Item("Қалқан", 30)]
inv2 = [Item("Қылыш", 50), Item("Айбалта", 80)]  # "Қылыш" қайталанып тұр

result = analyze_inventory([inv1, inv2])

print(f"Бірегей заттар жиыны (Set): {result['unique_items']}")
print(f"Ең қуатты зат (Top Power): {result['top_power']}")