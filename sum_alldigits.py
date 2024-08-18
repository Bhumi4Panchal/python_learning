#write a progarm to take two number from user add find sum for all digist between given number.
a = int(input("enter the a:"))
b = int(input("enter the b:"))
sum = 0
for i in range(a, b+1):
    sum += i
print("The sum of all digits between a and b is:",sum)

