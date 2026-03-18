#3
a = [5, -2, 8, 0, -7, 3]
def process_numbers(a):
    on= filter(lambda x: x>=0, a)
    b = map(lambda x: x/2 if x%2 == 0 else x * 3 +1, on)
    for i in b:
        yield i
for x in process_numbers(a):
    print(x)