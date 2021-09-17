'''
@Author: Rashmi
@Date: 2021-09-16 12:00:31
@Last Modified by: Rashmi
@Last Modified time: 2021-09-17 13:30:30
@Title : User Input and Replace String Template
         “Hello <<UserName>>, How are you?”

'''
import re

str = "Hello <<UserName>>, How are you?"
name = input("enter the name")

if re.match("^[A-Z]{1}[a-z]{2,}$", name):
      new_str = str.replace("<<UserName>>", name)
      print(new_str)  
else:
    print("invalid name")
