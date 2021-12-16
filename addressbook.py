"""
* @Author: Sachin S Kore
* @Date: 2021-12-16
* @Title : Adding Address Book Adding and Display
"""

from loghandler import logger
from validation import Validation


class AddressBook:

    def remove(self):
        pass

    def update(self):
        pass

    def display(self):
        """
          Description:
              This method is used for displaying address book details from object attributes
          Parameter:
              It takes for loop to get address book details stored inside list and
              display all the stored details.

          """
        if len(list) >= 1:
            logger.info("Data in the file is Given below: \n")
            print(
                'Id \t\t\t\t Name \t\t\t\t  Mobile \t\t\t\t\t Adress \t\t\t\t Zipcode \t\t\t\t City \t\t\t\t  State \n')
        for person in list:
            print(person.id, "\t\t\t\t", person.name, "\t\t\t\t",
                  person.mobile, "\t\t\t\t", person.address, "\t\t\t\t",
                  person.zip, "\t\t\t\t", person.city, "\t\t\t\t",
                  person.state, "\n")
            print("----------------------------------------------------------------------------------------------->")


class Contact:

    def __init__(self, id, name, mobile, address, zip, city, state):
        self.id = id
        self.name = name
        self.mobile = mobile
        self.address = address
        self.zip = zip
        self.city = city
        self.state = state


if __name__ == '__main__':
    print("Welcome To Address Book...")
    list = []
    while True:
        address = AddressBook()

        choice = int(input(' Press \n 1. To Add new contact \n 2. To Delete\n 3. To Update address book\n'
                           ' 4. To Print Book \n' ' 5. To Quit \n '))  # Asks user for input
        if choice == 1:
            """
             Description:
                 This option is used for adding a address book details in address book.
                 it creates a object and add details into it and then append them to a list.
             """
            id = Validation.validate_id()
            name = Validation.validate_name()
            mobile = Validation.validate_mobile()
            address = Validation.validate_address()
            zip = Validation.validate_zip()
            city = Validation.validate_city()
            state = Validation.validate_state()
            contact = Contact(id, name, mobile, address, zip, city, state)
            list.append(contact)
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
