c,b = map(int,input().split())
red = 0
green = 0
blue  = 0
black = 0
for i in range(1,c+1):
    for j in range (1,b+1):
        a = j*i
        if a % 5 == 0:
            blue += 1
        elif a % 3 == 0:
            green += 1
        elif a % 2 == 0:
            red += 1
        else:
            black +=1
print('RED',":",red)
print('GREEN',':',green)
print('BLUE',":",blue)
print('BLACK',":",black)