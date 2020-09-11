a = int(input())
klets = []
if a > 8 :
    klets.append(a - 8)
if a <= 56:
    klets.append(a + 8)
if a % 8 != 1:
    klets.append(a - 1)
if a % 8 != 0:
    klets.append(a + 1)
klets.sort()
print(*klets)