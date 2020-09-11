k,w = map(int,input().split())
answers =[]
w1,k1,w2,k2,w3,k3 = map(int,input().split())
if w1 + w2 <= w and k1 + k2 >= k:
    print('YES')
elif w3 + w2 <= w and k3 + k2 >= k:
     print('YES')
elif w1 + w3 <= w and k1 + k3 >= k:
    print('YES')
elif w1 + w2 +w3 <= w and k1 + k2 + k3 >= k:
    print('YES')
elif w1 <= w and k1 >= k:
    print('YES')
elif w2 <= w and k2 >= k:
    print('YES')
elif w3 <= w and k3 >= k:
    print('YES')
else:
    print('NO')
