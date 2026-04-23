# 3
class Item:
    def __init__(self, id, name, power):
        self.id = id
        self.name = name.strip().title()
        self.power = power

    def __hash__(self):
        return hash(self._id)

    def __eq__(self, other):
        if self._id == other._id:
            return True
        else:
            return False

    def __str__(self):
        return f"Init(id = {self.id}, name = '{self.name}', power = {self.power})"


i = Item(1, " Sword ", 50)
print(i)
