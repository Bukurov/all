a  = list(input())
b = 0
c = 0
for i in range(len(a)):
    if a[i] == '0':
        b += 1
    else:
        if b > c:
            c = b
        b = 0
if b > c:
    c = b
print(c)