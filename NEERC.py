a = int(input())
b = list(map(int,input().split()))
c = int(input())
print(sum(list(map(lambda x: x if x<c else c,b))))