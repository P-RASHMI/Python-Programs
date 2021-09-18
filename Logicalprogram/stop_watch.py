'''
@Author: Rashmi
@Date: 2021-09-18 18:10
@Last Modified by: Rashmi
@Last Modified time: 2021-09-18 18:45
@Title :  A Stopwatch Program for measuring the time that elapses between
the start and end clicks

'''
import time

if __name__ == '__main__':

    print("press enter to start and ctrl+c to stop time")

    while True:                 #loop for the input for enter and key interruption
        
        try:                                            

            input()                    #takes input 
            starttime = time.time()
            print('time started')

        except KeyboardInterrupt:         #interruption occurs when ctrl + c

            print('time Stopped')
            endtime = time.time()
            elapsed_time = endtime - starttime
            print("Elapsed time in seconds is : ", round(elapsed_time, 2))
            break


 

