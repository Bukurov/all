number_lines_page,number_of_lines = map(int,input().split())
if number_of_lines == 0:
    print(0,0)
else:
    string = number_of_lines % number_lines_page
    page = number_of_lines // number_lines_page
    if string != 0:
        page += 1
    else:
        string = number_lines_page
    
    print(page,string)
