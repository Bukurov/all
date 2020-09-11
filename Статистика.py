n = int(input())
list_days = list(map(int, input().split()))
list_days_even = list(filter(lambda x: x%2 == 0,list_days))
list_days_odd = list(filter(lambda x: x%2 == 1,list_days))
print(*list_days_odd)
print(*list_days_even)
if len(list_days_even) >= len(list_days_odd):
    print("YES")
else:
    print("NO")