# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 09:25:23 2022

@author: Guruprasada
"""

num = int(input("Enter the Number:"))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print("The Given number is {} and Reverse is {}".format(temp, reverse))