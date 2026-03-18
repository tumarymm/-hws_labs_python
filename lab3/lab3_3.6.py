#6
a = list(range(1, 21))
b = [
    "FizzBuzz" if i%3 == 0 and i%5 ==0
    else "Buzz" if i %5 == 0
    else "Fizz" if i %3==0
    else i
    for i in a
]
print(b)