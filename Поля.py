a,b = map(int,input().split())
c = a*b
c = c ** 0.5
if int(c) - c == 0:
    print(int(c))
else:
    print(0)