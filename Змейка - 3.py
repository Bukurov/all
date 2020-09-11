n, m, y, x = map(int,input().split())
a = list(range(m*y-m,m*y))
s = y % 2
b ={0:a.reverse(),
    1:None}
b[s]
print(a[x-1])
print(a)