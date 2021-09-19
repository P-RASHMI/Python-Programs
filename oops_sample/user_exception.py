'''
@Author: Rashmi
@Date: 2021-09-19 23:22
@Last Modified by: Rashmi
@Last Modified time: 2021-09-19 23:30
@Title :  sample program to raise customized exception

'''
if __name__ == '__main__':

    class UserException(Exception):               #create userdefined exception class and inherit exception
         
         def __init__(self,msg):
             self.msg = msg
         
         def print_exception(self):
             print("generated exception is : ",self.msg)

    try:
        raise UserException("crash of program")

    except UserException as e:
         e.print_exception()
             