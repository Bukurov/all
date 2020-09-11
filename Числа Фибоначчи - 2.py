a = int(input())
b,c = 1,1
f = 2
while True:
    f += 1
    b,c = c,b + c
    if c == a:
        print(1,'\n',f,sep = '')
        break
    if c > a:
        print(0)
        break
