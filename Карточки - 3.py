a = float(input())
c = 2
longcard = 0
while True:
    longcard += 1/c
    if a <= longcard:
        print(c-1,'card(s)')
        break
    c += 1