#Casandra Villagran
#2/20/2020

#Use a for statement to calculate the factorial of a user input x value
#Print this value as well as the calculated value using the factorial function in the math module

import math

number = int(input("enter the number: "))
fac = 1

for i in range(1,number + 1):
    fac = fac * i
print ("factorial of", number , " is ", fac) 
