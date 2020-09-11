a = input()
b,a = a[0],int(a[1])
abcd = {'A':1,
        'B':2,
        'C':3,
        'D':4,
        'E':5,
        'F':6,
        'G':7,
        'H':8}
a = a % 2
b = abcd[b] % 2
if a == 0 and b == 0:
    print('BLACK')
elif a != 0 and b != 0:
    print('BLACK')
else:
    print('WHITE')