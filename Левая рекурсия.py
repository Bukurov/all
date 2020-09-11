a = int(input())
score = 0
for i in range(a):
    left,right  = input().split('->') 
    t = right.find(left)
    if t == 0  :
        score += 1 
print(score)
