a,acd = map(int,input().split())
m = input()
if m ==  'fan':
    print(a)
elif m == 'auto':
    print(acd)
elif m == 'freeze':
    if a < acd:
        print(a)
    else:
        print(acd)
else:
    if a > acd:
        print(a)
    else:
        print(acd)
