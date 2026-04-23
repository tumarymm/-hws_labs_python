#17
class Player:
    def __init__(self, name):
        self.name = name
        print(f"Player {self.name} жасалды.")

    def __del__(self):
        print(f"Player {self.name} жойылды")




p1 = Player("Maksat")

print("Қазір Maksat-ты өшіреміз...")
del p1

print("Программа аяқталды.")