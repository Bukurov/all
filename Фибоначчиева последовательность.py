n , a , b = map(int,input().split())
if n == 1:
    print(a,b)
else:
    while n >= 2:
        a,b = b - a,a
        n -= 1
    print(a,b)