'''
@Author: Rashmi
@Date: 2021-09-20 17:10
@Last Modified by: Rashmi
@Last Modified time: 2021-09-20 17:17
@Title :  sample program to perform Concept of inner class and calling inner class values,inner class

'''


class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    def show(self):
        print(self.name,self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = 'Dell'
            self.cpu = 'i5'
            self.ram = 8
            print(self.brand,self.cpu,self.ram)
s1 = Student('Rashmi',1)
s2 = Student('Ravali',2) 
s1.show()
s1.lap.brand
#other way
lap1 = s1.lap
lap2 = s2.lap
#calling inner class 
lap1 = Student.Laptop()

            