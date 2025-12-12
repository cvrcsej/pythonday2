a = int(input())

if (a > 90):
    print(f"{a} A grade")
elif (a >= 80):
    print(f"{a} B grade")
elif (a >= 70):
    print(f"{a} C grade")
elif (a >= 60):
    print(f"{a} D grade")
elif (a >= 50):
    print(f"{a} E grade")
else:
    print("Fail")

match a // 10:
    case 10 :
        print(f"{a} A grade")
    case 9 :
        print(f"{a} A grade")
    case 8 :
        print(f"{a} B grade")
    case 7 :
        print(f"{a} C grade")
    case 6 :
        print(f"{a} D grade")
    case 5 :
        print(f"{a} E grade")
    case _ :
        print("fail")
        
        
    