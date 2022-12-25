# 4.Write a Python Program to Check Armstrong Number?

number = input("Enter the number you want to check : ")
n = 0 
for i in number :
    n = n + 1

s = 0
for j in number:
    s = s + int(j)**n

if int(s) == int(number):
    print("The given number is an Armstrong number.")
else:
    print("The given number is not an Armstrong number.")