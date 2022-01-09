# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 13:40:11 2022

@author: Guruprasada

"""
lower_limit = int(input("enter a lower number: "))
upper_limit = int (input("enter a upper limit: "))
sum = 0
for i in range (lower_limit,upper_limit+1):
    sum= sum+i
print("Sum of the number is", sum)