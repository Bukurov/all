a = input()
letters = ['q','w','e','r','t','y','u','i','o','p',
           'a','s','d','f','g','h','j','k','l',
           'z','x','c','v','b','n','m']
index = letters.index(a)
if index + 1 == 26:
    print('q')
else:
    print(letters[index + 1])
