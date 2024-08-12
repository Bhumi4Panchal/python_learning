#write a program to check if given number divisble by 3 and 5.
a = int(input("Enter the number:"))
if a % 3 == 0 and a % 5 == 0:
    print(a,"is number divisble to 3 and 5 ")
else:
    print(a,"isn't number divisble to 3 and 5 ")
