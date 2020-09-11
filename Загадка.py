a,b = map(int,input().split())
d = 0
i = 1
while a >= i:
    d = b / i
    if i+d == a:
        print(int(min(i,d)),int(max(d,i)))
        break 
    i+=1