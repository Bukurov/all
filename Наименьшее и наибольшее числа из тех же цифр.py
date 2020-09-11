a = list(map(int,(list(input()))))
a.sort()
for i in range (len(a)):
    if a[i] > 0:
        x = a[i]
        a.remove(x)
        a.insert(0, x)
        break
print(*a,sep = '',end= " ")
a.sort()
a.reverse()
print(*a,sep = '')