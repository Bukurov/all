n = int(input())
mass = list(map(int, input().split()))
k = int(input())
for i in range(k):
    s,f = map(int, input().split())
    if s != f:
        print(*mass[s-1:f])
    else:
        print(mass[s-1])
    
