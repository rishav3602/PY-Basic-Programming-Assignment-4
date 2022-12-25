# 3.Write a Python Program to Print the Fibonacci sequence?

n = int(input("Enter the number you want as 'Fibonacci sequence' : "))

fibbo = 0
nacci = 1
for i in range(n):
    print(fibbo)
    series = fibbo
    fibbo = nacci 
    nacci = series + fibbo

