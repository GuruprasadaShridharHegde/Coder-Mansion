# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 19:24:34 2022

@author: Guruprasada
"""

side= int(input("Enter side of square: "))
print("Square star pattern")
for i in range(side):
    for i in range(side):
        print("*", end="")
    print()