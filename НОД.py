a,b = map(int,input().split())
a,b = max(a,b),min(a,b)
while a%b!=0:
    t = a%b
    a = b
    b = t
print(b)
