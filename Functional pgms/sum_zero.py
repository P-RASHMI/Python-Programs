'''
@Author: Rashmi
@Date: 2021-09-18 10:38:11
@Last Modified by: Rashmi
@Last Modified time: 2021-09-18 11:17
@Title : A program to calculate the sum of triples equals to zero and
 print that triples

'''
def sum_zero_three(list,num_list):

    """to calculate the three numbers that equals to zero
       parameter : list of values and length of list .list,num_list
       return value : numbers of 3 """
    element_matched = False

    for i in range(0,num_list-2): #for first to last 2 digit

        for j in range(i+1,num_list-1): #for last 1 digit

            for k in range(j+1,num_list): # for last digit

                if(list[i]+list[j]+list[k] == 0):
                    print(list[i],list[j],list[k])
                    element_matched = True
    
    if (element_matched == False):
        print("the elements given are not making zero")

num = int(input("enter number of elements"))
list = []

for i in range(0,num):
    elements = int(input("enter elements"))
    list.append(elements)
num_list = len(list)

sum_zero_three(list,num_list)
