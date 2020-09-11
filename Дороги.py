a = int(input())
SUM = 0
for i in range(a):
    s = list(map(int,input().split()))
    for i in range(len(s)):
        if s[i] == 1:
            SUM += 1
print(int(SUM/2))
