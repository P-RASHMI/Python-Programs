'''
@Author: Rashmi
@Date: 2021-09-22 20:00
@Last Modified by: Rashmi
@Last Modified time: 2021-09-23 22:20
@Title :  Inventory management program > Create a JSON file having Inventory Details for Rice, Pulses and Wheats
with properties name, weight, price per kg.to calculate the Inventory Price 


'''
import json
from LoggerHandler import logger

class InventoryManagement:

    def __init__(self,Ingredient_list):
        self.Ingredient_list = Ingredient_list

    def add_ingredient(self):
        
        '''
        Discription :
                        This function is to create a Ingredient dictionary and store it                         
        '''
        try:
            num_of_cont = int(input("Enter the number of ingredients you want to store :"))
   
            for i in range(num_of_cont): # Used to count the number of ingredients to add in a dictionary
                name_of_ingredient = input("Enter the name of ingredient(Rice,Wheat,Pulses) : ")
                if self.Ingredient_list.get(name_of_ingredient) is not None: 
                    # ingredient name should be unique so it check address book name is already exist or not
                    break
                else:
                    self.Ingredient_list[name_of_ingredient] = {} 
                    name = str(input("Enter name : "))
                    self.Ingredient_list[name_of_ingredient]['Name'] = name
                    price = int(input("Enter price per kg : "))
                    self.Ingredient_list[name_of_ingredient]['Price'] = price
                    logger.info("added details of ingredients")
        except ValueError as e:
            print("Enter the Correct Value")
            logger.error("enter valid option")

    def write_in_json(self):

        '''
        Discription :
                        This function is to write the  Ingredient dictionary into json file store it                         
        '''
        try:
            json_object = json.dumps(self.Ingredient_list, indent=2)
            with open("oops_sample/InventoryManagement/InventoryDetails.json","w") as filewr:
                filewr.write(json_object)
                logger.info("File created and saved successfully")
        except Exception as e:
            print("not suitable",e)
            logger.error("Exception occured : ",type(e).__name__)
        finally:
            filewr.close()

    def read_from_json(self):

        '''
        Discription :
                        This function is to read the  Ingredient dictionary from json file store it                         
        '''
        try:
            with open ("oops_sample/InventoryManagement/InventoryDetails.json","r") as jsonfile:
                json_object = json.load(jsonfile)
                print(json_object)
        except Exception as e:
            print("file not there to read")
            logger.error("File doesnt exist")

    def calculate_ingredient(self):
        '''
        Description:
            This function is used to fetch the required data(price) for calculation from the above
            created dictionary from json file 
        '''
        try:
            self.calculate_dic = {} #Empty dictionary to store the result
            num_of_ingredient = int(input("Enter for how many ingredients you want to calculate price : "))
            
            for i in range(num_of_ingredient):
            
                name_of_ingredient = input("Enter the name of ingredient you want : ")
                given_ingredient = int(input(f"Enter in kg of {name_of_ingredient}  : "))
                self.calculate_dic[name_of_ingredient] = {}
            
                if self.Ingredient_list.get(name_of_ingredient) is not None:
                    fetch_ingredient = self.Ingredient_list[name_of_ingredient]['Price']
                    print("price per kg is ",fetch_ingredient)
                    total = fetch_ingredient*given_ingredient
                    print(f"Total cost for {given_ingredient}kg of {name_of_ingredient} is :",total)
                    total_calci = f"Total cost for {given_ingredient}kg of {name_of_ingredient} is"
                    logger.info("added details of ingredients")
                    
                    for key,value in self.Ingredient_list[name_of_ingredient].items():
                        self.calculate_dic[name_of_ingredient][key] = value
                    print(self.calculate_dic)
                    self.calculate_dic[name_of_ingredient][total_calci] = total
                    print(self.calculate_dic)
        except Exception as e:
            print("invalid",e)
            logger.error(print("Exception occured ",type(e).__name__))  

    def write_json_second(self):
    
        '''
        Discription :
                        This function is to write the fetched wages                          
        '''
        try:
            json_object = json.dumps(self.calculate_dic, indent=2)
            with open("oops_sample/InventoryManagement/ManagemtDetails.json","w") as filewr:
                filewr.write(json_object)
                logger.info("File created and saved successfully")
        except Exception as e:
            print("not suitable",e)
            logger.error("Exception occured : ",type(e).__name__)
        finally:
            filewr.close()
    def display_ingredients(self):
        
        '''
        Discription :
                        This function is used to display all the ingredients list dictionary
                    
        '''
        print(self.Ingredient_list)
        