a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()
if a[0] == b [0] and a[1] == b [1] and a[2] == b [2]:
    print('Boxes are equal')
else:
    if a[0] >= b [0] and a[1] >= b [1] and a[2] >= b [2]:
        print('The first box is larger than the second one')
    elif a[0] <= b [0] and a[1] <= b [1] and a[2] <= b [2]:
        print('The first box is smaller than the second one')
    else:
        print('Boxes are incomparable')