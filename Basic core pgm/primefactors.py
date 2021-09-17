'''
@Author: Rashmi
@Date: 2021-09-16 11:28:31
@Last Modified by: Rashmi
@Last Modified time: 2021-09-17 13:51:00
@Title : Gives prime factors of a Number ”

'''

import math
def primefactors(num):
    """primefactors to generate prime factors of the given number
       parameter : n
       return value : int n factors"""

    while num % 2 == 0:
        print(2)
        num = num / 2
    for i in range(3,int(math.sqrt(num))+1,2):
        while ( num % i == 0 ):
            print (i)
            num = num / i
    if num > 2:
        print (num)        
num = int(input("Enter the number to get prime factors for "))
print("the primefactors for ",num, ":")
primefactors(num)