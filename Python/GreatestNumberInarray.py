# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# method 1
arr  = [10,20,30,40,50]
print(max(arr))
"""
"""
# method 2
a = [10,20,30,40,50]
a.sort()
print(a[-1])


# method 3
a = [10,20,30,40,50]
max_element = a[0]
for i in range(len(a)):
    if a [i] > max_element:
        max_element = a[i]
print(max_element)
        

