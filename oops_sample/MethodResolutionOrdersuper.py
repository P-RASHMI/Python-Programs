'''
@Author: Rashmi
@Date: 2021-09-20 18:22
@Last Modified by: Rashmi
@Last Modified time: 2021-09-20 18:45
@Title :  sample program to perform Concept of MRO(METHOD RESOLUTION ORDER) use of super keyword, inheritance

'''

class Computer:

    def __init__(self):
        print("this is in parent class Computer")

    def feature(self):
        print("this is feature in computer parent class")

class Laptop:
    
    def __init__(self):
        super().__init__()                                       #goes to parent class init method,if Laptop class 
        print("this is in child class laptop")                    #inherits Computer class with super 
        
    def show(self):
        print("this is inside child class")

    def feature2(self):
        print("this is second feature in Laptop child class")

class Person(Computer,Laptop):
    
    def __init__(self):
        super().__init__()                                   #goes to parent class init method left parent so executes computer class init
        print("this is in child class person")

a1 = Laptop()   
b1 = Person()                                                 #goes to Laptop init method
