fact = 1
num = int(input("Enter number to find factorial: "))
if num < 0:
    print("Factorial of negative no DNE.")
elif num == 0:
    print("Factorial of 0 i s 1")
else:
    while num > 0:
        fact = fact * num
        num = num - 1
    print(fact)






