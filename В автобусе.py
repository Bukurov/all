adult,children = map(int,input().split())
if adult == 0 :
    print('Impossible')
else:
    if children == 0:
        MAX = adult
    else:
        MAX = adult+children -1
    if children >= adult:
        MIN = children 
    else:
        MIN = adult  
    print(MIN,MAX)