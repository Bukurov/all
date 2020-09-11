a = int(input())
town = []
for i in range(a):
    s = list(input())
    town.append(s)
number = 0
for i in range(a):
    for j in range(a):
        if town[i][j] == 'C':
            number += 1
lp = [1,2]
k = 0
C_number = 0
for i in range(a):
    for j in range(a):
        if town[i][j] == 'D':
            town[i][j] = lp[k]
        else:
            C_number += 1
            town[i][j] = lp[k]
            if C_number*2 == number:
                k+= 1
    print(*town[i],sep = '')
            

