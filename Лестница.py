a = int(input())
i = 1
while True:
    a -=i
    if a < 0:
        print(i-1)
        break
    else:
        i += 1