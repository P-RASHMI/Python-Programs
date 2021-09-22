'''
@Author: Rashmi
@Date: 2021-09-21 19:10
@Last Modified by: Rashmi
@Last Modified time: 2021-09-21 22:17
@Title :  sample program to perform CREATE DELETE UPDATE DISPLAY CONTACTS of Address Book

'''


class AddressBook:

    def __init__(self,Address_Book) :
            self.a = Address_Book
            
    def add_contact(self):

        '''
        Discription :
                        This function is to create a Address Book and store it 
                        into the dictionary. 
        '''
        try:
            num_of_cont = int(input("Enter the number of contacts you want to add :"))
   
            for i in range(num_of_cont): # Used to count the number of persons to add in address book
                name_of_addresbook = input("Enter the name of address book : ")
                if self.a.get(name_of_addresbook) is not None: 
                    # Address book name should be unique so it check address book name is already exist or not
                    #logger.error("Entred Address book is already exist : ")
                    break
                else:
                    
                    self.a [name_of_addresbook] = {} 

                    first_name = str(input("Enter your first name : "))
                    self.a [name_of_addresbook]['First Name'] = first_name

                    last_name = str(input("Enter your last name : "))
                    self.a [name_of_addresbook]['Last Name']  = last_name

                    address = str(input("Enter your Address : "))
                    self.a[name_of_addresbook]['Address'] = address

                    city = str(input("Enter your city name : "))
                    self.a [name_of_addresbook]['City'] = city

                    state_name = str(input("Enter your state name : "))
                    self.a [name_of_addresbook]['State'] = state_name

                    pin_code = int(input("Enter your pincode : "))
                    self.a [name_of_addresbook]['Zip Code'] = pin_code

                    contact = int(input("Enter your contact : "))
                    self.a [name_of_addresbook]['Phone Number'] = contact

                    email = str(input("Enter your email : "))
                    self.a [name_of_addresbook]['Email'] = email
        except ValueError as e:
            print("Enter the Correct Value")
            exit

    def edit_contact(self):
        '''
        Description:
            This function edit the contact details of person from Address Book.
            Here we edit details using the name of Address Book name. 
        '''
        try:
            name_of_addresbook = input("Enter the name of address book which you want to edit : ")
            attribute = int(input("Attribute to be Updat\n1:First Name\n2:Last Name\n3:Address\n4:City Name\n5:State Name\n6:Zip Code\nContact Number\n"))
            new_value = input("Enter new value : ")
            if attribute == 1:
                self.a [name_of_addresbook]['First Name'] = new_value
            elif attribute == 2:
               
                self.a [name_of_addresbook]["Last Name"] = new_value
            elif attribute == 3:
             #   new_value = input("Enter the address : ")
                self.a [name_of_addresbook]["Address"] = new_value
            elif attribute == 4:
              #  new_value = Validation.name_validation()
                self.a [name_of_addresbook]["City"] = new_value
            elif attribute == 5:
             #   new_value = Validation.name_validation()
                self.a [name_of_addresbook]["State"] = new_value
            elif attribute == 6:
              #  new_value = Validation.validate_zip()
                self.a [name_of_addresbook]["Zip Code"] = new_value
            elif attribute == 7:
              #  new_value = Validation.phone_number_validation()
                self.a [name_of_addresbook]["Phone Number"] = new_value
            elif attribute == 8:
                  #  new_value = Validation.phone_number_validation()
                self.a [name_of_addresbook]["Email"] = new_value
        except Exception as e:
            print("give valid details",e)
            self.edit_address_book()
            
    def delete_contact(self):
        '''
        Description:
            This function delete the contact details of person from Address Book.
            Here we delete details using the name of Address Book name. 
        '''
        try:
            name_of_addresbook = input("Enter the name of address book which you want to delete : ")
            del self.a [name_of_addresbook]
        except ValueError as e:
            print("Kindly Provide valid info : ",e)
            self.delete_contact()

    def display_contact(self):
        
        '''
        Discription :
                        This function is used to display the content of Address_Book dictionary
                        i,e the contact details of the person
        '''
        print(self.a)