a , b = map(int,input().split())
pole = []
strok = []
for i in range (b+2):
    strok.append('.')
pole.append(strok)
for i in range (a):
    s = list(str(input()))
    s.insert(0,'.')
    s.append('.')
    pole.append(s)
pole.append(strok)
score = 0
for  i in range (1,a+1):
    for j in range(1,b+1):
        if pole[i][j] == '.' and pole[i+1][j] == '.' and pole[i-1][j] == '.' and pole[i][j+1] == '.' and pole[i][j-1] == '.':
            score += 1
print(score) 