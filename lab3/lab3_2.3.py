#3
def infinite_numbers():
    n =1
    while True:
        if n % 3 == 0 and n % 5 == 0:
            yield "FizzBuzz"
        elif n % 3 == 0:
            yield "Fizz"
        elif n % 5 == 0:
            yield "Buzz"
        else:
            yield n
        n = n +1
a = infinite_numbers()
for i in range(15):
    print(next(a))