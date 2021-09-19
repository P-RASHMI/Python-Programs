'''
@Author: Rashmi
@Date: 2021-09-19 22:10
@Last Modified by: Rashmi
@Last Modified time: 2021-09-19 22:17
@Title :  sample program to perform calculator using oops concept of class methods 

'''

if __name__ == '__main__':


    class Calculator:

        def add(self, a, b):
            return a+b
        
        def subtract(self, a, b):
            return a-b
            
        def multiply(self, a, b):
            return a*b

        def divide(self, a, b):
            return a/b

    #create a calculator object
    calci = Calculator()

    while True:

        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")
        print("5: Exit")
        
        opt = int(input("Select operation: "))
        
        #Make sure the user have entered the valid choice
        if opt in range(1,6):    #1 t0 5
            
            if(opt == 5): #exit
                break
            
            #If not then ask fo the input and call appropiate methods        
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            
            if(opt == 1):
                print(a, "+", b, "=", calci.add(a, b))
            elif(opt == 2):
                print(a, "-", b, "=", calci.subtract(a, b))
            elif(opt == 3):
                print(a, "*", b, "=", calci.multiply(a, b))
            elif(opt == 4):
                print(a, "/", b, "=", calci.divide(a, b))
        
        else:
            print("Invalid Input")