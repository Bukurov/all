a,b = map(int,input().split())
letter =[]
for i in range(a):
    s = list(input())
    letter.append(s)

number = []
for i in range(a):
    s = list(map(int,input().split()))
    number.append(s)
dictionary ={
 0:lambda x : x == '.',
 1:lambda x : x == 'B' or x == '.',
 2:lambda x : x == 'G' or x == '.',
 3:lambda x : x == 'B' or x == 'G'  or x == '.',
 4:lambda x : x == 'R' or x == '.',
 5:lambda x : x == 'R' or x == 'B'  or x == '.',
 6:lambda x : x == 'R' or x == 'G' or x == '.',
 7:lambda x : True
}
def cikl():
    for i in range (a):
        for j in range(b):
                lewer = dictionary[number[i][j]](letter[i][j])
                if lewer == False:
                    print('NO')
                    return
    print('YES')
cikl()
            




