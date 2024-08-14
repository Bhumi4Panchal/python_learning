#make calculator using user input
no1 = int(input("Enter the no1:"))
operation = input("Enter operation (+, -, *, /,%): ")
no2 = int(input("Enter the no2:"))
if operation == '+':
    result = ("Addition is :",no1 + no2)
elif operation == '-':
    result = ("Subtraction is :",no1 - no2)
elif operation == '*':
    result = ("Mul is :",no1 * no2)
elif operation == '%':
    result = ("Module is :",no1 % no2)
elif operation == '/':
        result = ("Divide is :",no1 / no2)
else:
    result = "Invalid operation"
print("The result is:", result)

