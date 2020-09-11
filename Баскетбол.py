team = 0
teem = 0
for i in range(4):
    M,K = map(int,input().split())
    team += M
    teem += K
if team > teem :
    print(1)
elif teem > team:
    print(2)
else:
    print('DRAW')

    
            

