a = int(input())
big = a* 6
small = a // 6
ost = a % 6
if ost == 1:
    small +=6
elif ost == 2:
    small +=5
elif ost == 3:
    small +=4
elif ost == 4:
    small +=3
elif ost == 5:
    small +=2
print(small,big)

