n,s = map(int,input().split())
sale  = list(map(int,input().split()))
a = 0
ssum  = 0
number = 0
while True:
    a = min(sale)
    sale.remove(a)
    ssum +=a
    number+= 1
    if ssum > s:
        number -=1
        break 
print(number)

