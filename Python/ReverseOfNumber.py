# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 17:27:33 2022

@author: Guruprasada
"""
## using slicing
"""
num = 1231689
print(str(num)[::-1])
"""
## Using while loop
num = int(input("Enter the Number: "))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print("The Given number is {} and Reverse is {}".format(temp, reverse))


