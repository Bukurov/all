def get_big_small(number):
    list_diget = list(map(int,str(number)))
    while len(list_diget) < 4:
        list_diget.insert(0,0)
    big = list(list_diget)#6000
    big.sort()#0006
    small = list(big)#0006
    big.reverse()#6000
    big ,small = list(map(str,big)),list(map(str,small))
    big = int(''.join(big))
    small = int(''.join(small))
    return big,small


number  = int(input())
count = 0
while True:
    big,small = get_big_small(number)
    mid = big - small
    if mid == number:
        break
    number = mid
    count += 1
print(number)
print(count)