'''
@Author: Rashmi
@Date: 2021-09-19 2:24
@Last Modified by: Rashmi
@Last Modified time: 2021-09-19 3:12
@Title :  Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.

'''
import random
def coupons_derivation():

    """Description :to calculate generated distinct coupons from the userinput
       parameter : number of coupons generated (number)
       printing value : distinct coupons and its count"""

    coupon = []
    random_numbers=0  #no.of random numbers which are distinct
    try:

        number=int(input("Enter The Number Of Coupons: ")) 
        print("Distinct Coupon Numbers Generated")
        for i in range(number):
            coupon_number = random.randint(10,100)       #here change in parameters
            if coupon_number not in coupon: #Checking the number is present in list or not
                coupon.append(coupon_number)  #adding the distinct random number gnerated to list 
                random_numbers+=1
                print(coupon_number)       
                          
        print("random numbers which generated Distinct Numbers:",end = " ")
        print(random_numbers)

    except ValueError as e:                    #when floating values are passed value error raises
                print("error in values",e)

if __name__ == '__main__':
    coupons_derivation()