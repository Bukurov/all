a  = int(input())
time_list = {}
second_list =[]
for i in range(a):
    time = list(map(int,input().split()))
    second = time[0] * 3600 + time[1] * 60 + time[2]
    time_list[second] = time 
    second_list.append(second)
second_list.sort()
for i in range(a):
    print(*time_list[second_list[i]])

