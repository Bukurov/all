a = int(input())
c = list(map(int,input().split()))
score = 0
before = c[0]
for i in range(len(c)-1):
    if c[i + 1] != before + 1:
        score += 1
    before = c[i + 1]
print(score) 