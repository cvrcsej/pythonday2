p = input("enter password: ")

l = len(p)
if (l>=10):
    print("Strong")
elif (l > 8):
    print("Medium")
else:
    print("week")
