k = int(input())
d = 0
for i in range(k):
    f = int(input())
    if f == 0:
        d += 1
print(min(d,k-d))
