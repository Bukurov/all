m,v,d = map(int,input().split())
m = m // 2
v = v // 6
if m < v:
    if m < d:
        print(m) 
    else:
        print(d)
else:
    if v < d:
        print(v)
    else:
        print(d)
    
