#6
numbers = [0, -3, 5, -7, 8]
r = lambda x:"on" if x >0 else ("teris" if x<0 else "nol")
a = [r(n) for n in numbers]
print(a)