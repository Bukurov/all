sus = list(map(int,input().split()))
dog = list(map(int,input().split()))
per = int(input())
kord = []
for i in range(per):
    s = list(map(int,input().split()))
    kord.append(s)
t = False
for i in range(per):
    tr_sus =[abs(sus[0] - kord[i][0]),abs(sus[1] - kord[i][1])]
    tr_dog =[abs(dog[0] - kord[i][0]),abs(dog[1] - kord[i][1])]
    sline =  (tr_sus[0]**2 + tr_sus[1]**2)**0.5
    dline =  ((tr_dog[0]**2 + tr_dog[1]**2)**0.5)/2
    if sline <= dline:
        print(i+1)
        t = True
        break
if t == False:
    print('NO')
