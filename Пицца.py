a = int(input())
if a == 1:
    print(2)
if a == 2:
    print(4)
else:
    k = 4
    for i in range(a - 2):
        k = k + 3 + i
    print(k)
    

    