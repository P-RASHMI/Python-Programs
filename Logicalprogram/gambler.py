'''
@Author: Rashmi
@Date: 2021-09-18 23:10
@Last Modified by: Rashmi
@Last Modified time: 2021-09-19 2:17
@Title :  Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. 

'''
import random

def gambler(stake,goal,number):

    """Description :to calculate wins, loss and percentage of wins,loss
       parameter : stake,goal,number(amount he had,win amount,bets)
       printing value : wins loss percentages and wins"""

    win_count = 0
    loss_count = 0
    counter = 0

    while (stake > 0 and stake < goal and counter < number):   
        try:
           counter+=1
           randum_generated = random.randint(0,1)    #if suppose randint(0,1,78) given three parameters generating type error exception

           if (randum_generated == 1):
               win_count = win_count + 1
               stake = stake + 1
           else:
               loss_count = loss_count + 1
               stake = stake - 1
        except TypeError as e:
                print("error found ", e )                     #to find type of exception type(e).__name__

    percent_win = (win_count/number)*100
    percent_loss = 100-percent_win
    print("Number of wins",win_count)
    print("win percentage :",percent_win)
    print("loss percentage :",percent_loss )
    print("Number of times betting done",counter)

if __name__ == '__main__':
    stake = int(input("Enter the stake amount :"))
    goal = int(input("Enter how much money want to win"))
    number = int(input("Enter number of times he want to get involved in betting"))
    gambler(stake,goal,number)