'''
@Author: Rashmi
@Date: 2021-09-20 22:46
@Last Modified by: Rashmi
@Last Modified time: 2021-09-25 23:10
@Title : Find employee present or absent,calculate daily wage part time or full time,use 
switcher,given part time hr is 8 and monthly days 20; calculate wages till a condition of total
working hours or days is reached for a month - Assume 100 hours and 20 days ,reading all 
constant values from json file
'''
import random
import json

class EmployeeWage:

    def __init__(self):
        pass
   
    def employee_wage(self,Attendance):
        '''Description : based on the attendance generated by random it switches to call full day or
        absent or half day function,from switcher.get()'''
        switcher = {
            0 : self.absent(),
            1 : self.full_day(),
            2 : self.half_day()
            }

        return switcher.get(Attendance)         # its dictionary it fetches value of the key 

    def read_from_json(self):
        '''Description : reads data from json file and calculates perday wages and monthly wages 
        increments days and hours'''
        hours = 0
        monthly_wage = 0
        days = 0
        with open ("oops_sample/Employeewage/EmployeeDetails.json","r") as file:
            self.emp_dict = json.load(file)
            print(self.emp_dict)
            while days < self.emp_dict["MONTHLY_DAYS"] and hours < self.emp_dict["MONTHLY_HR"]:
                Attendance = random.randint(0,2)
                per_day_wage = self.employee_wage(Attendance)
                print(per_day_wage)
                monthly_wage = monthly_wage + per_day_wage
                days += 1
                hours+=1
            print("the monthly wage of employee",monthly_wage)

    def full_day(self):
        '''Description : calculates full day wages by taking values from json file'''
        full_day_wage = self.emp_dict["FULL_DAY_HR"] * self.emp_dict["PER_HR_WAGE"]
        return full_day_wage

    def half_day(self):
        '''Description : calculates half day wages by taking values from json file'''
        half_wage = self.emp_dict["PART_TIME_HR"] * self.emp_dict["PER_HR_WAGE"]
        return half_wage

    def absent(self):
        '''Description: returns zero as employee is absent'''
        return 0

if __name__ == '__main__':
    
    employeewage = EmployeeWage()
    employeewage.read_from_json()