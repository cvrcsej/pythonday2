a = int(input('Enter an number'))

if (a % 2 == 0):
    print(f"{a} is  Even")
else:
    print(f"{a} is odd")
    
match a % 2:
    case 0:
        print(f"{a} is Even")
    case 1:
        print(f"{a} is odd")
