'''
@Author: Rashmi
@Date: 2021-09-21 19:10
@Last Modified by: Rashmi
@Last Modified time: 2021-09-21 22:10
@Title :  sample program to perform CREATE DELETE UPDATE DISPLAY CONTACTS of Address Book

'''
from AddressBookoperation import AddressBook                  #importing AddressBook class from AddressBookoperation file
Address_Book = {}                                             #Dictionary
book_obj = AddressBook(Address_Book)                   #passing dictionary into class and creating object for class

if __name__ == '__main__':
    try:   
        while(True):
            print("1.Add contacts in Address Book")
            print("2.Edit the contacts in Address Book")
            print("3.Delete the contacts from Address Book") 
            print("4.Display Address Book") 
            choice = int(input())            
            if choice == 1:
                book_obj.add_contact()
            elif choice == 2:
                book_obj.edit_contact()
            elif choice == 3:
                book_obj.delete_contact()
            elif choice == 4:
                book_obj.display_contact()
            else:
                break
    except ValueError as e:
            print("Invalid Input",e)

