# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 08:03:08 2022

@author: Guruprasada
"""

a = input("enter a number:  ")
b = a[::-1]
if a == b:
    print("pallindrome")
else:
    print("not pallindrome")