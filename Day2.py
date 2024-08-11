#1. area of circle
pi = 3.14
radius = float(input("Enter the radius of the circle: "))
area = pi*radius*radius
print("The area of the circle with radius is",area)

#2. area of rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle with length and width is",area)

#3. write a program simple interest and compound interest
principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
year = float(input("Enter the year:"))
simple_interest = (principal * rate_of_interest * year) / 100
print("Simple Interest:",simple_interest)
amount = principal+simple_interest
print("principal amount",amount)

compound_interest = principal * (1 + rate_of_interest / 100) ** year
print("Compound Interest:",compound_interest)
amount = principal+compound_interest
print("principal amount",amount)

#4. convert the temperature fahrenheit into celsius
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print("The temperature in Celsius is",celsius)

#5. to swap values of two varibles without using third varibles
a = int(input("Enter the a :"))
b = int(input("Enter the b:"))
a, b = b, a
#a=a+b , b=a-b ,a=a-b
print("After swapping a value:",a)
print("After swapping b value:",b)

#6. To identify varibles
striggg = "Hello python"
boolean = True
integer = 10
print(type(striggg))
print(type(boolean))
print(type(integer))

#7.even or odd number
a = int(input("enter the a number:"))
if (a%2 == 0):
    print(a,"is a even number")
else:
    print(a,"is a odd number")

#8. weather give number is positive , negative and 0
b = int(input("enter the b number:"))
if b>0:
    print("The number is Positive")
elif b<0:
    print("The number is negative")
else:
    print("The number is Zero")

#1. write a python program to print hello world.
#2. To identify varibles
#3. for addition of two strings
#4. to create simple calculator
#5. to swap values of two varibles without using third varibles
#6. to create calculator by taking user input
