'''
@Author: Rashmi
@Date: 2021-09-17 19:10:01
@Last Modified by: Rashmi
@Last Modified time: 2021-09-17 19:36:03
@Title : A program that takes a,d,c from quadratic equation and print the roots”

'''

import math
def deriveroots(a,b,c):
    """to calculate roots of quadratic equation
       parameter : a,b,c
       return value : roots"""

    #To find determinent
    detrimt = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(detrimt))

    if detrimt > 0:
        print("real and different")
        root1 = (-b + sqrt_val)/(2*a)
        root2 = (-b - sqrt_val)/(2*a)
        print("roots are: ", root1 , root2 )
    elif detrimt == 0:
        print("roots are real and same")
        print("root is", -b /(2*a))
    else:
        print("roots are complex")  
a = int(input("enter the x* x coefficient"))
b = int(input("enter the x coefficient"))
c = int(input("enter the constant"))
if (a == 0):
    print("give the corect quadratic equation")
else:
    deriveroots(a,b,c)
