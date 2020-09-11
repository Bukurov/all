a = int(input())
start = []
end = []
for i in range(a):
    s , b = map(int,input().split())
    start.append(s)
    end.append(b)
if max(start) > min(end):
    print('NO')
else:
    print('YES')