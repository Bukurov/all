M,K,N = map(int,input().split())
ALL = M + K - N
if ALL >= 0:
    print(ALL)
else:
    print('Impossible')
