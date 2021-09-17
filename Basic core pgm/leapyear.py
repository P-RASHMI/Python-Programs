'''
@Author: Rashmi
@Date: 2021-09-16 18:45:31
@Last Modified by: Rashmi
@Last Modified time: 2021-09-17 14:04:00
@Title : Given four digit year and the year is leap year or 
not is printed  ”

'''
year = int(input("Enter the year "))
if (year > 999 and year < 10000) :
   if((( year % 4 == 0 ) and ( year % 100 != 0)) or (  year % 400 == 0 )):
       print (year, " is leap year")
   else:
        print(year, "not a leap year")
else :
    print("enter a valid year")           