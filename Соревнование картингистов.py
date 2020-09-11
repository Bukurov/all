a,b = map(int,input().split())
name = None
ssum  = []
record_name = None
record = 100000000
for i in range (a):
    name = input()
    ssum = list(map(int,input().split()))
    if sum(ssum) < record:
        record_name = name
        record = sum(ssum)
print(record_name)
        