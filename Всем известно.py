a = input()
a = list(a)
b = False
for i in range(len(a)):
    if a[i] == '0':
        print('NO')
        b = True
        break
if b == False:
    print('YES')
    
