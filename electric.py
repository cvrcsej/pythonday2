a = int(input("Enter units: "))
b = a
if (b <= 100):
    print(b)
elif (b <= 300):
    rem = a - 100
    tv = 100
    tv += rem * 2
    print(tv)
else :
    c = 500
    rem = b - 300
    tv = c + (rem * 4)
    if (tv > 1000):
        tax = (tv / 100)*10
        print(tax)
        print(tax + tv)
        print(tv)

    