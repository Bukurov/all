M,K,N = map(int,input().split())
if M > 727 or K > 727 or N > 727:
    print('Error')
    exit(0)
if M < 94 or K <  94 or N <  94:
    print ('Error')
    exit(0)
elif N > M:
    if N > K: 
        Big = N
    else:
        Big = K
else:
    if M > K:
        Big = M
    else:
        Big = K
if Big != None :
    print (Big)
else:
    print (M)
