n,m,f,l = map(int,input().split())
both_exam = (n - l - m - f)*-1
print(both_exam,m - both_exam,f - both_exam)
