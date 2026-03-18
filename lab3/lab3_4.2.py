#2
a = ["кот", "машина", "арбуз", "дом", "ананас"]
b = [ (lambda x:(x.upper() if len(x)>4 else "short") + ("*" if "a" in x else ""))(i) for i in a]
print(b)
