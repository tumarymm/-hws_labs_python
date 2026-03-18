# 2. Генераторы (4 задачи)
# 1Жұп сандар және 4-ке бөлінуі
def even_numbers(n):
    for x in range(1, n + 1):
        if x % 2 == 0:
            yield "4ke eselik" if x % 4 == 0 else x


for x in even_numbers(10):
    print(x)
