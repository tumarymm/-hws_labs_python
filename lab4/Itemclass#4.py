# 4
class Item:
    def __init__(self, item_id, name):
        self.id = item_id
        self.name = name

    def __repr__(self):
        return f"{self.name}({self.id})"


class Inventory:
    def __init__(self):

        self.items = []

    def add_item(self, item):

        for existing in self.items:
            if existing.id == item.id:
                print(f" Қате: {item.id} нөмірлі зат бұрыннан бар!")
                return
        self.items.append(item)
        print(f" {item.name} қосылды.")

    def remove_item(self, item_id):

        self.items = [i for i in self.items if i.id != item_id]
        print(f" {item_id} нөмірлі зат жойылды.")

    def get_items(self):
        return self.items

    def to_dict(self):

        return {i.id: i for i in self.items}


my_bag = Inventory()
my_bag.add_item(Item(1, "Қылыш"))
my_bag.add_item(Item(2, "Қалқан"))
my_bag.add_item(Item(1, "Тағы бір қылыш"))

print(f"Сөмкедегі заттар: {my_bag.get_items()}")