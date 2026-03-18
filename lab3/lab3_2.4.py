# 4
def squares(a):
    for i in range(1, a + 1):
        n = i ** 2
        yield "жұп квадрат" if n % 2 == 0 else n


for b in squares(5):
    print(b)
