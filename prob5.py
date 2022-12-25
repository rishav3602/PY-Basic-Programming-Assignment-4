# 5.Write a Python Program to Find Armstrong Number in an Interval?

lower_limit = int(input("Enter the lower limit of the interval : "))
upper_limit = int(input("Enter the upper limit of the interval : "))
arm_list = list()

for i in range(lower_limit,upper_limit+1):
    number = str(i)
    n = 0 
    for j in number :
        n = n + 1

    s = 0
    for k in number:
        s = s + int(k)**n

    if int(s) == int(number):
        arm_list = arm_list + [i]

print(f"List of  Armstrong numbers from {lower_limit} to {upper_limit} is : {arm_list}")
    
