# 6.Write a Python Program to Find the Sum of Natural Numbers?

n = int(input("Enter the value of number : "))
for i in range (1,n+1):
    sum =  i*(i+1)/2
print(f"The sum of {n} natural numbers is : {sum}")