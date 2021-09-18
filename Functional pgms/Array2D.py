'''
@Author: Rashmi
@Date: 2021-09-18 2:05:11
@Last Modified by: Rashmi
@Last Modified time: 2021-09-18 10:38:01
@Title : A program that takes rows and columns to print 2d array
'''

def array_two(rows_number,columns_number):

    """to print array taking rows and columns
       parameter : rows_number,columns_number
       return value : printing matrix format"""
  
# matrix
    matrix = [] 
    print("Enter the entries row wise:") 
  
# For user input 
    for i in range(rows_number):          #  for loop for row entries 
        a =[] 
        for j in range(columns_number):      #  for loop for column entries 
            a.append(int(input())) 
        matrix.append(a) 
  
# For printing the matrix 
    for i in range(rows_number): 
        for j in range(columns_number): 
            print(matrix[i][j], end = " ") 
        print() 

rows_number = int(input("Enter the number of rows:")) 
columns_number = int(input("Enter the number of columns:")) 
array_two(rows_number,columns_number) 