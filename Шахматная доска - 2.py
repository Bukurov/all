m, n, i, j, c = map(int,input().split())
if c == 1:
    win = 'white'
    over = 'black'
else:
    win = 'black'
    over = 'white'
if m % 2 == 0 or n % 2 == 0:
    print('equal')
#m и n не четные
else:
    if j % 2 == 1 and i % 2 == 1 or j % 2 == 0 and i % 2 == 0:
        print(win)
    else:
        print(over)