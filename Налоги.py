a = int(input())
listf = list(map(int,input().split()))
listp = list(map(int,input().split()))
for i in range(len(listp)):
    if listp[i] != 0:
        listp[i] = listp[i] / 100
record  = -1
for i in range(len(listf)):
    local_record = listf[i] * listp[i]
    if local_record > record:
        record = local_record 
        index = i + 1
print(index)
