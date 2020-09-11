n = int (input())
fib1 = fib2 = 1
if n < 2:
    print(1)
else:
    """for i in range(n):
        print(fib1 )
        fib1,fib2 = fib2 ,(fib1+fib2) %10
    print(fib1 )"""
    nambers = []
    for i in  range(65):
        nambers.append(fib1)
        fib1,fib2 = fib2 ,(fib1+fib2) %10
    b = n % 60
    print(nambers[b])

    
    
