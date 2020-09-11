a  = int(input())
c = '2.7182818284590452353602875'
b = list(c)
if a == 0:
    print(3)
elif a == 25:
    print(c)
else:
    if int(b[a+2]) >= 5:
        b[a+1] = str(int(b[a+1])+1)
    for i in b[:a+2]:
        print(i,end = '' )