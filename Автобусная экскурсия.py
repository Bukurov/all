a =int(input())
b = list(map(int,input().split()))
p = 437
for i in range(len(b)):
    if p >= b[i]:
        print('Crash',i+1)
        break
    if p <b[i] and i+1 == len(b):
        print('No crash')

