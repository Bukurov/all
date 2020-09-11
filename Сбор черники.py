a = int(input())
b = list(map(int,input().split()))
record = 0
for i in range(a):
    if i == 0:
        s = b[0]+b[-1]+b[1]
        if s > record:
            record = s
    elif i == a-1:
        s = b[0]+b[-1]+b[-2]
        if s  > record:
            record = s
    else:
        s = b[i-1]+b[i]+b[i+1]
        if s  > record:
            record = s
print(record)

