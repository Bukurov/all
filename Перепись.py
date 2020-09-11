a = int(input())
year = 0
number = -1
for i in range(a):
    b,c = map(int,input().split())
    if c == 1 and year < b:
        year = b
        number = i+1
print(number)


