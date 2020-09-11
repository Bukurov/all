a = list(input())
col = 0
for i in range(len(a)- 4):
    if a[i] == '>' and a[i+1] == '>' and a[i+2] == '-' and a[i+3] == '-' and a[i+4] == '>' or a[i] == '<' and a[i+1] == '-' and a[i+2] == '-' and a[i+3] == '<' and a[i+4] == '<': 
        col +=1
print(col)
