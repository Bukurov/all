n, m, d, k = map(int,input().split())
S_1 = (m+n)*d*k
S_2 = m*n * d*d
print(S_1 - S_2)