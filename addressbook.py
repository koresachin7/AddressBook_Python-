"""
* @Author: Sachin S Kore
* @Date: 2021-12-16
* @Title : Adding Address Book Adding and Display
"""
import json
import sys
from loghandler import logger
from validation import Validation


class AddressBook:

    def save(self):
        """
    Description:
        This method is writing or storing address book details from list into json file
    Parameter:
        It takes self as a parameter to get addressbook details stored inside list and
        using json dump it writes those details inside json file.

    """
        try:
            with open('addressbook.json', 'w+') as file:
                json.dump(list, file, indent=2)
                logger.info("file successfully saved...")

        except Exception as e:
            logger.error(e)

        finally:
            file.close()

    def remove(self):
        """
        Description:
            This method is used for deleting address book details
        """
        try:
            count = 0
            if len(list) >= 1:
                id = input("Enter Your Unique id : ")
                for delete in list:
                    if delete.id == id:
                        logger.info(" Data Removed Successfully ")
                        del list[count]
                        self.save()
                        return
                    count += 1

        except Exception as e:
            logger.error(e)

    def update(self):
        """
         Description:
             This method is used for update address book details from list
         """
        if len(list) >= 1:
            id = input("Enter Your Unique id : ")
            for i in list:
                if i.id == id:

                    if True:
                        option = int(
                            input(
                                "Select Any One Option to update your Profile\n 1 First Name \n 2 Mobile Number \n 3 "
                                "Address \n 4 Zipcode \n 5 city \n 6 state \n "))

                        if option == 1:
                            name = Validation.validate_name()
                            self.save()
                            i.name = name

                        elif option == 2:
                            mobile = Validation.validate_mobile()
                            i.mobile = mobile
                            self.save()

                        elif option == 3:
                            address = Validation.validate_address()
                            i.address = address
                            self.save()

                        elif option == 4:
                            zip = Validation.validate_zip()
                            i.zip = zip
                            self.save()

                        elif option == 5:
                            city = Validation.validate_city()
                            i.city = city
                            self.save()

                        elif option == 6:
                            state = Validation.validate_state()
                            i.state = state
                            self.save()

                        else:
                            print("Invalid Option")
                            self.update()

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

    def __init__(self, add_new):
        self.id = add_new.get("id")
        self.name = add_new.get("name")
        self.mobile = add_new.get("mobile")
        self.address = add_new.get("address")
        self.zip = add_new.get("zip")
        self.city = add_new.get("city")
        self.state = add_new.get("state")


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
            add_new = {"id": id, "name": name, "mobile": mobile, "address": address, "zip": zip, "city": city, "state": state}
            contact = Contact(add_new)
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
            address.save()
            logger.info(" Data is Currently Displaying ")
        elif choice == 6:
            logger.info(" Bye User ")
            exit()
