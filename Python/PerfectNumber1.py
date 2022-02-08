# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:05:25 2022

@author: Guruprasada
"""
# Perfect Numbers

def divisiors(x): 
    return [y for y in range(1, int(x / 2) + 1) if x % y == 0] 
 
def perfect_numbers_in_range(a,b): 
    return [x for x in range(a,b+1) if sum(divisiors(x)) == x] 
 
print(perfect_numbers_in_range(1, 1000)) 
 