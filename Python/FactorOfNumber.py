# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 16:55:03 2022

@author: Guruprasada
"""
# Factor of a number 
num  = int(input("enter a number: "))
for i in range(1, num+1):
    if num % i == 0:
        print(i, end = " ")