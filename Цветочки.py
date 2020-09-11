a = int(input())
flowers =['G','C','V']
for i in range(a):
    flowers[2],flowers[1] = flowers[1],flowers[2]
    flowers[0],flowers[1] = flowers[1],flowers[0]
print(flowers[0],flowers[1],flowers[2],sep = '')
