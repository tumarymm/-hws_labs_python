#5
a =  [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
def matrix_transform(a):
    for i in a:
        for j in i:
            if j % 2 == 0 and j %3== 0:
                yield "кратно 6"
            elif j%2 == 0:
                yield "чётное"
            elif j%3 == 0:
                yield "кратно 3"
            else:
                yield j
for x in matrix_transform(a):
    print(x)