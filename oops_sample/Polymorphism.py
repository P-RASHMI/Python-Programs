'''
@Author: Rashmi
@Date: 2021-09-20 17:10
@Last Modified by: Rashmi
@Last Modified time: 2021-09-20 17:17
@Title :  sample program to perform method overriding of polymorphism, inheritance of  oops 

'''

class Computer:

    def show(self):
        print("this is in parent class")

    def feature(self):
        print("this is feature in computer parent class")

class Laptop(Computer):

    def show(self):
        print("this is inside child class")

   # def feature(self):
   #     print("this is feature in Laptop child class")

    def feature2(self):
        print("this is second feature in Laptop child class")

com1 = Computer()          
com2 = Laptop()
com1.show()               #calls show method of computer class
com2.show()                #calls show method of Laptop class
com2.feature()             #calls feature of parent class as child inherits parent