a = int(input())
record = 0
local_record = 0
c = list(map(int,input().split()))
for i in range (len(c)):
    if c[i] > 0 :
        local_record += 1
    else:
        local_record = 0
    if local_record > record:
        record = local_record 
    
print(record)