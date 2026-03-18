#2
a =  ["кот", "машина", "арбуз", "дом"]
b = list(map(lambda x: x.upper() + "!" if len(x)> 3 else x.upper(), a))
print(b)