# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 21:11:58 2022

@author: Guruprasada
"""

num = int(input("Enter the Number:"))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=",")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")