a = list(input())
for b in range(1,101):
    k = b
    for i in range(len(a)):
        if a[i] == '1':
            b += 1
        elif a[i] == '2':
            b -= 1
        if b > k :
            k = b
        if b <= 0 :
            t  = False
            break 
        else:
            t  = True 
    if t == True:
        break
print(k)