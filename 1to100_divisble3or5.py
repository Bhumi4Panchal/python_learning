#write a program display between 1 to 100 those are divisble by 3 or 5.
a = 1
while a <= 100:
    if a % 3 == 0 or a % 5 == 0:
        print(a)
    a += 1