Basic = int(input("Enter basic salary: "))
print(Basic)

HRA = (Basic / 100) * 20
DA = (Basic / 100) * 10

tv = Basic + HRA + DA
print(tv)

if(Basic >= 50000):
    Tax = (tv / 100) * 10
else:
    Tax = (tv / 100) * 5
    
print(HRA)
print(DA)
print(Tax)
pay = tv - Tax
print(pay)