# 6
from datetime import datetime


class Event:
    def __init__(self, e_type, data):
        self.type = e_type
        self.data = data
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"Event(type = {self.type}, data = {self.data} , timestamp = {self.timestamp})"


e1 = Event("ATTACK", {"damage": 20})
print(e1)

e2 = Event("HEAL", {"hp_added": 15})
print(e2)
