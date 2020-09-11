r = int(input())
list_time = list(map(int,input().split()))
p3 = list_time.copy()
p1 = list_time.copy()
p3.reverse()
p1.sort()
def counting(time_list,kurs):
    penal_time = 0
    time = 0
    task_p = 0
    for i in time_list:
        if time  + i > 300:
            return task_p,penal_time,kurs
        time += i 
        penal_time += i
        task_p += 1
    return task_p,penal_time,kurs
result_list = [counting(list_time,5),counting(p3,3),counting(p1,1)]        
result_list.sort()
if result_list[0][0] == result_list[-1][0]:
    print(result_list[0][2])
elif result_list[1][0] < result_list[-1][0]:
    print(result_list[-1][2])
else:
    print(result_list[1][2])
        
    
