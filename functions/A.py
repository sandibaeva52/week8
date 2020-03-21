a=int(input())
b=int(input())
c=int(input())
d=int(input())
def minimum(a,b,c,d):
    return min(min(min(a,b),c),d)

print(minimum(a,b,c,d))
