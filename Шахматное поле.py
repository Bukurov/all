x1,y1,x2,y2 = map(int,input().split())

x1 = x1 % 2
y1 = y1 % 2

x2 = x2 % 2
y2 = y2 % 2

if x1 == 0 and y1 == 0:
    one ='BLACK'
elif x1 != 0 and y1 != 0:
    one ='BLACK'
else:
    one ='WHITE'

if x2 == 0 and y2 == 0:
    two ='BLACK'
elif x2 != 0 and y2 != 0:
    two ='BLACK'
else:
    two ='WHITE'

if two == one:
    print('YES')
else:
    print('NO')
