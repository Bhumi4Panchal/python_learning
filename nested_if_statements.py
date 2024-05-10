x = input("Enter the number:")
print("Number is " ,x)
if (int(x) < 0):
     print("Number is Negative")
elif(int(x) > 0):
    if(int(x) <= 100 ):
        print("This Number is under 100")
    elif(int(x) < 100):
        print("This Number is not under 100")
    else:
        print("Number is greater than 100")
