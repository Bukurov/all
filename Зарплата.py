M,K,N = map(int,input().split())

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

print (Big)
