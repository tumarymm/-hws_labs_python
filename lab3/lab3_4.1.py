#Смешанные сложные задачи (5 штук)
#1
def is_prime(x):
    if x<2:
        return False
    for i in range(2, x):
        if x%i==0:
            return False
    return True
def special_numbers(n):
    for i in range(1, n +1):
        if i%3 == 0 and i%5==0:
            yield "FizzBuzz"
        elif i%5 == 0:
            yield "Buzz"
        elif i%3 == 0:
            yield "Fizz"
        elif is_prime(i):
            yield "простое"
        else:
            yield i

for x in special_numbers(15):
    print(x)