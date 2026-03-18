#4
a =  [0, 5, 12, 7, 20, -3, 8]
b = list(map(lambda x: x/2 if x%2==0 else x*3, filter(lambda x: x> 5, a)))
print(b)