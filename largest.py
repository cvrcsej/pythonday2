a,b,c = int(input("Enter 3 numbers: ").split(""))

if (a > b and a > c):
    print(f"{a} a is greater")
elif (b > c and b > a):
    print(f"{b} is greater")
else:
    print(f"{c} is greater")
    
match True:
    case _ if a > b and a > c:
        print(f"{a} a is greater")
    case _ if b > a and b > c:
        print(f"{b} is greater")
    case _:
        print(f"{c} is greater")