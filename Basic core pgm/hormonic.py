'''
@Author: Rashmi
@Date: 2021-09-16 22:12:31
@Last Modified by: Rashmi
@Last Modified time: 2021-09-17 14:07:00
@Title : Print the Nth Hormonic number and N! = 0 ”

'''
def harmonic(num):
    """harmonic to generate harmonic value of the given number
       parameter : num
       return value : harmonic number"""
    if num < 2:
        return 1
    else:
       return 1 / num + (harmonic(num-1))
num = int(input("enter the number"))
if (num == 0):
    print("given value should not be zero ")
else:
    print("the hormonic number is", (harmonic(num)))

    