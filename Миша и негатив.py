a,b = map(int,input().split())
white = []
black = []
error = 0
for i in range(a):
    c =list(str(input()))
    white.append(c)
aed = input()
for i in range(a):
    c =list(str(input()))
    black.append(c)
for i in range(a):
    for j in range(b):
        if white[i][j] == black[i][j]:
            error += 1
print(error)