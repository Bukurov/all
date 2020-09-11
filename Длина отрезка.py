a,b,c,d = map(int,input().split())
dl = ((a-c)**2+(b-d)**2)**0.5
if dl < 0:
    print(dl * -1)
else:
    print(dl)
