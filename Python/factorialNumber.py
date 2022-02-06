# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 08:49:14 2022

@author: Guruprasada
"""

num = int(input("Enter a number: "))
factorial = 1
if num<0:
    print("Enter a positive number")
elif num ==0:
    print("The factorial of 0 is one")
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print("factorial of",num,"is", factorial)