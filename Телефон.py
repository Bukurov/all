a,b,c,d = map(int,input().split())
if a > d:
    a = d
il_time = d - a
time = d - il_time
money = time * b + il_time *c
print(money)
