a = int(input())
def code_2(a):
    list_a =[]
    p = 0
    b = True
    while b:
        if a >= 2:
            list_a.append(a % 2)
            a = a//2
        else:
            list_a.append(a)
            b = False
    for i in list_a:
        p +=i
    return p
g = code_2(a)
print(a+g)
