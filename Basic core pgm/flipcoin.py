'''
@Author: Rashmi
@Date: 2021-09-16 23:11:31
@Last Modified by: Rashmi
@Last Modified time: 2021-09-17 14:11:00
@Title : Number of times flip the coin and get heads, tails percentage ”

'''
import random
heads = 0
tails = 0
counter = 0
flips = int(input("Enter number of times coin to be tossed"))
while ( counter < flips ):
    toss = random.random()
    print("counter:",counter,"RandomNum:",toss)
    if (toss < 0.5):
        heads = heads + 1
        print(heads)
    else : 
        tails = tails + 1
        print(tails)
    counter = counter + 1
print("number of heads:",heads)
print("number of tails:",tails)
headpercent = (heads * 100) / flips
tailpercent = (tails * 100) / flips
print("heads percentage:",headpercent)
print("tails percentage:",tailpercent)