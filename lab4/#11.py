#11
def damage_stream(events):
    for event in events:
        if event["type"] == "ATTACK":
            yield event["damage"]
events = [
    {"type" : "ATTACK" , "damage": 10},
    {"type" : "HEAL", "amount": 5},
    {"type" : "ATTACK", "damage" : 7}
]
for i in damage_stream(events):
    print(i)