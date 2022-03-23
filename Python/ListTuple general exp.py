# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:58:25 2022

@author: Guruprasada
"""
a = [1,2,3]
b = [1,2,3]
print (a is b)

c = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print (c[1:19:2]) ## starting, ending, interval
print(c[::-1])

print(a + [4,5,6,7,8,9,10])
print(a*3)

d = ['mango', 'orange', 'lime', 1 , 2 , 3 , 4 , 5]
d[0] = 'moosumbe'   
print(d)
d[0:3] = ['sapota']
print(d)