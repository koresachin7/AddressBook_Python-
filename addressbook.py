"""
* @Author: Sachin S Kore
* @Date: 2021-12-9
* @Title : Adding Address Book Data
"""

from loghandler import logger
from validation import Validation


class AddressBook:

    def __init__(self, list):
        self.list = list

    def remove(self):
        pass

    def update(self):
        pass

    def display(self):
        pass


class Contact:

    def __init__(self):
        pass


if __name__ == '__main__':
    print("Welcome To Address Book...")
    # list = []
    while True:
        address = AddressBook(list)
        contact = Contact()
        choice = int(input(' Press \n 1. To Add new contact \n 2. To Delete\n 3. To Update address book\n'
                           ' 4. To Print Book \n' ' 5. To Quit \n '))  # Asks user for input
        if choice == 1:
            contact.add()
            logger.info(" Data Added Successfully ")  # if user input is 1 the add a data
        elif choice == 2:
            address.remove()
            logger.info(" Data Removed Successfully ")  # if user input is 2 then delete a data
        elif choice == 3:
            address.update()
            logger.info(" Data Updated Successfully ")  # user input is 3 to update the data
        elif choice == 4:
            address.display()
            logger.info(" Data is Currently Displaying ")  # user input is 4 to print the AddressBook
        elif choice == 5:
            logger.info(" Bye User ")
            exit()
