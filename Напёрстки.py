a = input()
b = [1,0,0]
for i in range(len(a)):
    if a[i] == 'A':
        b[1],b[0] = b[0],b[1]
    elif a[i] == 'B':
        b[1],b[2] = b[2],b[1]
    elif a[i] == 'C':
        b[0],b[2] = b[2],b[0]
print( b.index(1)+1)
