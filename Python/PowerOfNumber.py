# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 12:47:09 2022

@author: Guruprasada
"""

base = int(input("enter a base number:  "))
expo = int(input("enter a exponential number:  "))
temp = 1
for i in range (0, expo):
    temp= base * temp
print(temp)