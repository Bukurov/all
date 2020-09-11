pol = []
for i in range (4):
    a = list(input())
    pol.append(a)
lewer = True
for i in range(3):
    for j in range(3):
        #if pol[i][j] == "W" and pol[i][j + 1] == "W" and pol[i+1][j] == "W" and pol[i+ 1][j + 1] == "W" or pol[i][j] == "B" and pol[i][j + 1] == "B" and pol[i+1][j] == "B" and pol[i+1][j + 1] == "B":
        if pol[i][j] ==  pol[i][j + 1] == pol[i+1][j] == pol[i+ 1][j + 1]:
                print('No')
                lewer = False
                break
if lewer == True:
    print('Yes')
                
