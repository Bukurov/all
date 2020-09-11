n,m = map(int,input().split())
a = list(map(int,input().split()))
sell = 0
for i in range (m):
    local_max = max(a)
    if local_max <= 0:
        break
    sell += local_max
    a.remove(local_max)
print(sell)