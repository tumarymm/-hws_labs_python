#3
a = ["кот", "машина", "ананас", "дом"]
b = []
for i in a:
    if len(i) > 4 and "a" not in i:
        b.append(i)
print(b)