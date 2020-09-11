a = int(input())
a6 = a % 10
a5 =(a // 10) % 10
a4 =(a // 100) % 10
a3 =(a // 1000) % 10
if a6 == a3 and a5 == a4:
    print('YES')
else:
    print('NO')
