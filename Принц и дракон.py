a,b,c = map(int,input().split())
if a < b and a <= c:
    print('NO')
elif a >= b:
    print(1)
else:
    i = 0
    while True:
        i+=1
        b -=a
        if b <= 0:
            print(i)
            break
        b += c