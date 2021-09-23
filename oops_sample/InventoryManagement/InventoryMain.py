'''
@Author: Rashmi
@Date: 2021-09-22 20:00
@Last Modified by: Rashmi
@Last Modified time: 2021-09-23 22:20
@Title : Inventory management program > Create a JSON file having Inventory Details for Rice, Pulses and Wheats
with properties name, weight, price per kg.to calculate the Inventory Price 

'''

from LoggerHandler import logger
from InventoryOperation import InventoryManagement
Ingredient_list = {}
ingredient_obj = InventoryManagement(Ingredient_list)


if __name__ == '__main__':
    try:   
        while(True):
            print("1.Add ingredients ")
            print("2.read from json")
            print("3.Get the price of ingredients") 
            print("4.display")
            print("5.write into json\n6.write into second json")
            choice = int(input())            
            if choice == 1:
                ingredient_obj.add_ingredient()
            elif choice == 2:
                ingredient_obj.read_from_json()
            elif choice == 3:
                ingredient_obj.calculate_ingredient()
            elif choice == 4:
                ingredient_obj.display_ingredients()
            elif choice == 5:
                ingredient_obj.write_in_json()
            elif choice == 6:
                ingredient_obj.write_json_second()

            else:
                break
    except ValueError as e:
            print("Invalid Input",e)
            logger.error("enter valid option")