# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 08:12:49 2022

@author: Guruprasada
"""

year = int(input("enter a year:  "))
if(((year%4==0))) & (year %100 !=0) | (year %400==0):
    print({year},"is a leap year")
else:
    print({year},"not a leap year")