a = input()
b = '1'
nul = ''
for i in range (1,len(a)):
    if a[-i] == '0':
        nul += '0'
    else:
        break
b += nul
print(int(b))
