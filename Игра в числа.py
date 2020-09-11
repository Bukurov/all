a = int(input())
s = list(map(int,input().split()))
list_numbers  =[0,0]#second,first
i = 0
while len(s) != 0:
    i += 1
    if s[0] >= s[-1]:
        list_numbers[i % 2] += s[0]
        s.pop(0)
    else:
        list_numbers[i % 2] += s[-1]
        s.pop(-1)
print(list_numbers[1],':',list_numbers[0],sep ='')
