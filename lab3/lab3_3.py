#3Тізімнен тек 10нан үлкен және жұп сандарды қалдыру
numbers = [5, 12, 7, 20, 33, 8]
r = list(filter(lambda x: x % 2 == 0 and x>10, numbers))
print(r)