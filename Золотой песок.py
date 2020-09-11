A,B,C,D,I,F = map(int,input().split())

def biggest(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
             return b
        else:
             return c

def normal(a,b,c,e,w):
    if a == e and b == w or a == w and b == e:
        return c
    elif c == e and b == w or c == w and b == e:
        return a
    elif c == e and a == w or c == w and a == e:
        return b


def small(a,b,c):
    if a < b:
        if a < c:
            return a
        else:
            return c
    else:
        if b < c:
             return b
        else:
             return c

big = biggest(A,B,C),biggest(D,I,F)
smal = small(A,B,C),small(D,I,F)
norm =normal(A,B,C,big[0],smal[0]),normal(D,I,F,big[1],smal[1])
money = big[0]*big[1]+norm[0]*norm[1]+smal[0]*smal[1]
print(money)

    
