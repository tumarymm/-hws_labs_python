#14
class Player:
    def __init__(self, hp, inventory):
        self.hp = hp
        self.inventory = inventory


decide_action = lambda p: "HEAL" if p.hp < 30 else ("LOOT" if not p.inventory else "ATTACK")




p1 = Player(hp=20, inventory=["Sword"])
print(f"Ойыншы 1 шешімі: {decide_action(p1)}")

p2 = Player(hp=80, inventory=[])
print(f"Ойыншы 2 шешімі: {decide_action(p2)}")


p3 = Player(hp=100, inventory=["Shield"])
print(f"Ойыншы 3 шешімі: {decide_action(p3)}")