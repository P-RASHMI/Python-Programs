'''
@Author: Rashmi
@Date: 2021-09-19 23:10
@Last Modified by: Rashmi
@Last Modified time: 2021-09-19 23:17
@Title :  sample program to perform calculator using oops concept of inheritance

'''
if __name__ == '__main__':
    
    class Calculator:

        def add(self,a,b):
            first_num = input("enter first element")
            second_num = input("enter second element")
            print("addition of numbers method from base class ", first_num + second_num)
 
    calci = Calculator()
    class Child(Calculator):

        def __init__(self,numberoftimes):
            print("in child class")
            self.numberoftimes = 9
        def  result(self):
             print("done with child class")
            
        calci.add


                    
