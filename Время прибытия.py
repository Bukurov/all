hours ,mint = map(int,input().split(':'))
plhours,plmint = map(int,input().split())
'{:0>2}'.format(2)
hours += plhours
mint += plmint
plhours = mint //60
mint = mint % 60
hours += plhours
hours = hours % 24
print('{:0>2}'.format(hours),':','{:0>2}'.format(mint),sep = "")

