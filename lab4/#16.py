#16
class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self.id = player_id
        self.name = name
        self._hp = hp
        self._inventory = []

    @property
    def hp(self):
        return self._hp

    @property
    def inventory(self):
        return list(self._inventory)

    def update_hp(self, amount: int):
        self._hp += amount
        if self._hp < 0:
            self._hp = 0
        print(f" {self.name} денсаулығы: {self._hp}")

    def add_to_inventory(self, item: str):
        self._inventory.append(item)
        print(f"{item} сөмкеге салынды.")

p = Player(1, "Алдияр", 100)

print(f"Бастапқы HP: {p.hp}")

p.update_hp(-40)
p.add_to_inventory("Алтын қылыш")

print(f"Инвентарь: {p.inventory}")