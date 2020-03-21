from math import sqrt
a=int(input())
b=int(input())
for i in range(a, b+1):
    square = float(sqrt(i))
if(square*square==i):
    print(i)