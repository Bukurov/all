a = int(input())
b = list(map(int,input().split()))
c = b[0]
b.pop(0)
if a == 2:
    print(min(b))
else:
    MIN = min(b)
    b.remove(MIN)
    ost1 = c - b[0]
    ost2 = c - b[1]
    MIN = MIN - ost1 - ost2
    if MIN >= 0:
        print(MIN)
    else:
        print(0)