#Casandra Villagran
#2/20/2020

#Write a program to compute the approximation and then print
#that value as well as the value of math.pi from the math module.

import math
sum = 0
for i in range(1,5000000):
    sum=sum+1/(i**2)
print(math.sqrt(6*sum))

print(math.pi)
