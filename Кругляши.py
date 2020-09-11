a = list(input())
b = 0
for i in range(len(a)):
    if a[i] == '8':
        b += 2
    elif a[i] == '6' or a[i] == '0' or a[i] == '9':
        b += 1
print(b)