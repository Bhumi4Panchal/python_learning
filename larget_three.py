#write the program to find larget number among give the three numbers.
no1 = int(input("enter the no1:"))
no2 = int(input("enter the no2:"))
no3 = int(input("enter the no3:"))
if no1 >= no2 and no1 >= no3 :
    print(no1,"is largest number")
elif no2 >= no3 and no2 >= no1:
    print(no2,"is largest number")
else:
    print(no3,"is largest number")
