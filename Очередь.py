a  = int(input()) -1
kas  = 720 
klient = a
ost_time = kas - klient * 5
if ost_time < 0 :
    print('NO')
else:
    kas = kas - ost_time
    hours = kas // 60
    minuts = kas % 60
    print(hours,minuts)