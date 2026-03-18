#2
a = [[1,2,3],[4,5,6],[7,8,9]]
b = [(lambda i: i[0]*i[1]*i[2])(i) for i in a]
print(b)