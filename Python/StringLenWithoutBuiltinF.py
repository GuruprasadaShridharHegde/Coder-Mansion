# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:14:55 2022

@author: Guruprasada
"""

string = input("enter the length of a string:  ")
count = 0
for i in string:
    count+= 1
print(count)
if count<1:
 print("invalid")
elif count>10:
 print("Large string")
else:
 print("Small string")
 