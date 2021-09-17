'''
@Author: Rashmi
@Date: 2021-09-16 15:28:55
@Last Modified by: Rashmi
@Last Modified time: 2021-09-17 14:00:012
@Title :  This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N.where  0 <= N < 31 ”

'''
num = int(input("Enter THE NUMBER"))
if ( num < 31):
    for i in range(num + 1):
        print(2 ** i)
else:
    print("give the range less than 31")
   
