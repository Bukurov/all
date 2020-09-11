a,b = map(int,input().split())
c = a // b
s = a % b
clist = []
for i in range (b):
    clist.append(c)
for i in range(s):
    clist[i] += 1
clist.reverse()
print(*clist)

