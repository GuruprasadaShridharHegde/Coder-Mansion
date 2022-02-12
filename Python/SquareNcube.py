# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 11:11:02 2022

@author: Guruprasada
"""

import _thread # import the thread module  
import time # import time module  
  
def cal_sqre(num): # define the cal_sqre function  
    print(" Calculate the square root of the given number")  
    for n in num:   
        time.sleep(0.3) # at each iteration it waits for 0.3 time  
        print(' Square is : ', n * n)  
  
def cal_cube(num): # define the cal_cube() function  
    print(" Calculate the cube of  the given number")  
    for n in num:   
        time.sleep(0.3) # at each iteration it waits for 0.3 time  
        print(" Cube is : ", n * n *n)  
        
  
arr = [2, 3, 4, 6]  # given array  
  
t1 = time.time() # get total time to execute the functions  
cal_sqre(arr) # call cal_sqre() function  
cal_cube(arr) # call cal_cube() function  
  
print(" Total time taken by threads is :", time.time() - t1) # print the total time  