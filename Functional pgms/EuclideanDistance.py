'''
@Author: Rashmi
@Date: 2021-09-17 18:08:55
@Last Modified by: Rashmi
@Last Modified time: 2021-09-17 18:41:012
@Title : A program that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function”

'''

import math
 
def calculateDistance(num1,num2):
    """to calculate distance of the point from origin
       parameter : num1,num2
       return value : dist"""
    dist = math.sqrt(num1 * num1 + num2 * num2)
    print("the distance is : " ,dist)
num1 = int(input(print("Enter x1 co-ordinate")))
num2 = int(input(print("Enter y1 co-ordinate")))
calculateDistance(num1,num2)
