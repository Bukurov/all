a,b = map(int,input().split())
MAX = max(a,b)
while True:
    if a % MAX == 0 and b % MAX == 0:
        break
    MAX -=1
for i in range(MAX):
    print(1,end='')