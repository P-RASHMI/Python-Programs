'''
@Author: Rashmi
@Date: 2021-09-19 23:10
@Last Modified by: Rashmi
@Last Modified time: 2021-09-19 23:17
@Title :  sample program to perform calculator using oops concept of inheritance

'''

    
class Calculator:

    def __init__(self):
      #  self.a = a
       # self.b = b
        print("this is inside parent class")

    def add(self,a,b):
       
        print("value", a+b)

    
class Child(Calculator):

    def specific(self):
        print("in child class")
        
    def  result(self):
            print("done with child class")

if __name__ == '__main__':  
     
    a = int(input("enter a value"))
    b = int(input("enter b value"))      
    calci = Calculator()
    calci.add(a,b)
    
                    
