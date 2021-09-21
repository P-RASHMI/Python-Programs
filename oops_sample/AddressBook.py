'''
@Author: Rashmi
@Date: 2021-09-20 22:10
@Last Modified by: Rashmi
@Last Modified time: 2021-09-20 23:17
@Title :  sample program to perform CREATE DELETE UPDATE DISPLAY CONTACTS of Address Book

'''

# this function will be the first to run as soon as the main function executes
def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts: ")), 6
     
    phone_book = []
    print(phone_book)

    for i in range(rows):
       
        temp = []
        for j in range(cols):                  

            if j == 0:
                temp.append(str(input("Enter first name*: ")))
            if j == 1:
                temp.append(str(input("Enter last number*: ")))
            if j == 2:
                temp.append(str(input("Enter e-mail address: ")))                     
            if j == 3:
                temp.append(str(input("Enter city: ")))
            if j == 4:
                temp.append(str(input("Enter state: ")))
            if j == 5:
                temp.append(int(input("Enter pincode: ")))
            if j == 6:
                temp.append(int(input("Enter phone: ")))
                    
        phone_book.append(temp)                  # By this step we are appending a list temp into a list phone_book
                                                # That means phone_book is a 2-D array and temp is a 1-D array 
    print(phone_book)
    return phone_book
 
def menu():
    
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Update")
    print("5. Display all contacts")
    print("6. Exit phonebook")
    choice = int(input("Please enter your choice: "))
    return choice
 
def add_contact(pb):
                                                        # append another list of details into the already existing list
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter first name*: ")))
        if i == 1:
            dip.append(str(input("Enter last number*: ")))
        if i == 2:
            dip.append(str(input("Enter e-mail address: ")))
        if i == 3:
            dip.append(str(input("Enter city: ")))
        if i == 4:
            dip.append(str(input("Enter state: ")))
        if i == 5:
            dip.append(int(input("Enter pincode: ")))
        if i == 6:
            dip.append(int(input("Enter phone: ")))

    pb.append(dip)
                                                  # And once you modify the list, you return it to the calling function wiz main, here.
    return pb
 
def remove_existing(pb):

    query = str(input("Please enter the name of the contact you wish to remove: "))
    temp = 0
    # temp is a checking variable here. We assigned a value 0 to temp.
     
    for i in range(len(pb)):
        if query == pb[i][0]: # Temp will be incremented & it won't be 0 anymore in this function's scope
            temp += 1                                          #to print the deleted contact
            print(pb.pop(i))                                        
            print("This contact has now been removed")
            return pb
            
    if temp == 0:                     # temp will remain 0 and that means the contact does not exist in this phonebook
        print("enter the correct name")
        return pb

def delete_all(pb):
    return pb.clear()
def display_all(pb):
    if not pb:
        print("List is empty: []")
    else:
        for i in range(len(pb)):
            print(pb[i])                           # if display function is called after deleting all contacts then the len will be 0
                                                            # And then without this condition it will throw an error

 
ch = 1
pb = initial_phonebook()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_existing(pb)
    elif ch == 3:
        pb = delete_all(pb)
#   elif ch == 4:
#        d = Update(pb)
    elif ch == 5:
        display_all(pb)
    else:
         exit