a,b,c = map(int,input().split())
b,c = min(b,c) ,max(b,c)
one = c - b -1
two = a - c + b -1 
print(min(two,one))