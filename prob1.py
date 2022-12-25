# 1.Write a Python Program to Find the Factorial of a Number?

num = int(input("Enter your number : "))

factorial = 1
for i in range(1,num+1):
    factorial = factorial * i

print(f"The factorial of {num} is : {factorial}")