a = int(input())
b =list(map(int,input().split()))
local_balls = 3
score = 0
for i in range(a):
    if b[i] == 1:
        score += local_balls
        local_balls += 1
    else:
        local_balls -= 3
        if local_balls < 3:
            local_balls = 3
print(score)