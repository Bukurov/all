a,b = map(int,input().split())
area = []
for i in range(a):
    s = [1]*b
    area.append(s)
zero_area =[]
for i in range(a):
    s = [j*0 for j in range(b)]
    zero_area.append(s)
for i in range(a):
    for j in range(b):
        if zero_area[i][j - 1] > zero_area[i - 1][j]:
            zero_area[i][j] = zero_area[i][j - 1] + area[i][j]
        else:
            zero_area[i][j] = zero_area[i - 1][j] + area[i][j]
for i in range(len(zero_area)):
    print(zero_area[i])
a -= 1
b -= 1
put = [(a,b)]
while a != 0 and b != 0:
    if b >= 0  and zero_area[a][b-1] > zero_area[a-1][b] :
        b -=1
        put.append((a,b))
    elif a >= 0  and zero_area[a-1][b] >= zero_area[a][b-1]:
        a -= 1
        put.append((a,b))

if a == 0:
    while b != 0:
        b -= 1
        put.append((a,b))
else:
    while a != 0:
        a -= 1
        put.append((a,b))
print(put)