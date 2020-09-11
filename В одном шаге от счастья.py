b = int(input())
for i in range(b):
    a = input()
    if a == '000000' :
        print('YES')
    if a == '999999':
        print('YES')
        continue
    a_next = int(a)+ 1
    a_before = int(a)- 1
    list_next = list(map(int, f'{a_next:06}'))
    list_before = list(map(int, f'{a_before:06}'))
    if sum(list_next[:3])==sum(list_next[3:]) or sum(list_before[:3])==sum(list_before[3:]):
        print("YES")
    else:
        print("NO")