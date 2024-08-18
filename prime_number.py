#write a program to check weather given number is a prime number or not.
num = int(input("Enter the number:"))
for i in range(2, num):
    if num % i == 0:
        print(num,"is not a prime number.")
        break
else:
    print(num,"is a prime number.")

