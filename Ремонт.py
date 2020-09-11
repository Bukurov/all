A,B,C = map(int,input().split())
k = (C * B + C * A) * 2 
d = (k - 1)// 16 + 1

print(d)
