a,b = map(int,input().split())
a,b = min(a,b),max(a,b)
if b % 2 == 0:
    b = b//2
else:
    b = b//2 + b % 2
print(b,a)