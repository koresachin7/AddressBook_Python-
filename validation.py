import re
from loghandler import logger


class Validation:
    @staticmethod
    def validate_name():

        try:
            name = input("Enter your Name :")
            if re.match("^[A-Z]{1}[a-z]*$", name):
                return name
            else:
                logger.error("name should be alphabets")

        except ValueError:
            logger.error("Invalid input")

    @staticmethod
    def validate_mobile():

        try:
            mobile = input("Enter your Mobile Number :")
            if re.match("^[7-9]{1}[0-9]*$", mobile):
                return mobile
            else:
                logger.error("mobile number shpuld be numeric")

        except ValueError:
            logger.error("Invalid input")

    @staticmethod
    def validate_address():

        try:
            address = input("Enter your Address : ")
            if re.match("^[A-Z]{1}[a-z]+", address):
                return address
            else:
                logger.error("Address should be in alphabets")

        except ValueError:
            logger.error("Invalid input")

    @staticmethod
    def validate_zip():

        try:
            zip = input("Enter your zip :")
            if re.match("^[1-9]{1}[0-9]{5}$", zip):
                return zip
            else:
                logger.error("zip should be numeric")

        except ValueError:
            logger.error("Invalid input")

    @staticmethod
    def validate_city():

        try:
            city = input("Enter your city :")
            if re.match("^[A-Za-z]*$", city):
                return city
            else:
                logger.error("City should be alphabets")

        except ValueError:
            logger.error("Invalid input")

    @staticmethod
    def validate_state():

        try:
            state = input("Enter your state :")
            if re.match("^[A-Za-z]*$", state):
                return state
            else:
                logger.error("State should be in alphabets")

        except ValueError:
            logger.error("Invalid input")

    @staticmethod
    def validate_id():
        try:
            while True:
                id = input(" Enter unique id : ")
                if re.match("^[0-9]{2,3}$", id):
                    return id
                else:
                    logger.error("Enter valid id ")

        except ValueError:
            logger.error("Invalid input")
