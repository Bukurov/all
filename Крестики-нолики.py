a =[]
for i in range(3):
    s = list(str(input()))
    a.append(s)
def winorlose(k):
    t = False
    if k == a[0][0] and k == a[1][1] and k == a[2][2]:
        t = True
    if k == a[0][2] and k == a[1][1] and k == a[2][0]:
        t = True
    for i in range(3):
        if k == a[i][0] and k == a[i][1] and k == a[i][2]:
            t = True
            break
        if k == a[0][i] and k == a[1][i] and k == a[2][i]:
            t = True
            break
    return t
nul = winorlose('O')
krest = winorlose('X')
if krest == True:
    print('Win')
elif nul == True:
    print('Lose')
else:
    print('Draw')