a,b = input().split()
f = 0
a = int(a)
s =''
for i in list(b):
    f += 1
    if f != a :
        s += b[f-1]
print(s)
        
    
