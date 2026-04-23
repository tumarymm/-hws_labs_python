# 2
class Player:
    def __init__(self, player_id, name, hp):
        self._id = player_id
        self._name = name.strip().title()
        if hp < 0:
            hp = 0
        self._hp = hp

    def __str__(self):
        return f"Player(id = {self._id},name = '{self._name}', hp = {self._hp})"

    @classmethod
    def from_string(cls, data):
        parts = data.split(",")
        if len(parts) != 3:
            raise ValueError("qate format")
        p_id = int(parts[0].strip())
        p_name = parts[1].strip()
        p_hp = int(parts[2].strip())

        player = cls(p_id, p_name, p_hp)
        return player


p = Player.from_string("2, alice , 90")
print(p)
