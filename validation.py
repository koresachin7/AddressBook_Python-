import re
from loghandler import logger


class Validation:
    @staticmethod
    def validate_name(name):
        """
           Description:
                       This method is used for Validate name
           Parameter:
                    It takes first alphabets Capital letter and following are small letter
        """
        try:
            if re.match("^[A-Z]{1}[a-z]*$", name):
                return name
            else:
                logger.error("name should be alphabets")

        except ValueError:
            logger.error("Invalid input")

    @staticmethod
    def validate_mobile(mobile):
        """
           Description:
                       This method is used for Validate Mobile number
           Parameter:
                     It takes first digit between 7 to 9 and following are 0 to 9
        """
        try:
            while True:
                if re.match("^[7-9]{1}[0-9]{9}$", mobile):
                    return mobile
                else:
                    logger.error("mobile number shpuld be numeric")

        except ValueError:
            logger.error("Invalid input")

    @staticmethod
    def validate_address(address):
        """
           Description:
                       This method is used for Validate address
           Parameter:
                    It takes first alphabets Capital letter and following are small letter
        """
        try:
            while True:
                if re.match("^[A-Z]{1}[a-z]+", address):
                    return address
                else:
                    logger.error("Address should be in alphabets")

        except ValueError:
            logger.error("Invalid input")

    @staticmethod
    def validate_zip(zip):
        """
            Description:
                        This method is used for Validate zip code
            Parameter:
                    It takes first digit between 1 to 9 and following are 0 to 9 and total number are six
        """

        try:
            while True:
                if re.match("^[1-9]{1}[0-9]{5}$", zip):
                    return zip
                else:
                    logger.error("zip should be numeric")

        except ValueError:
            logger.error("Invalid input")

    @staticmethod
    def validate_city(city):
        """
           Description:
                      This method is used for Validate city name
        """

        try:
            while True:
                if re.match("^[A-Za-z]*$", city):
                    return city
                else:
                    logger.error("City should be alphabets")

        except ValueError:
            logger.error("Invalid input")

    @staticmethod
    def validate_state(state):
        """
           Description:
                    This method is used for Validate state name
        """

        try:
            while True:
                if re.match("^[A-Za-z]*$", state):
                    return state
                else:
                    logger.error("State should be in alphabets")

        except ValueError:
            logger.error("Invalid input")

    @staticmethod
    def validate_id(id):
        """
           Description:
                       This method is used for Validate id number
           Parameter:
                    It takes digit between 0 to 9 and limit of digit between 2 to 3
        """
        try:
            while True:
                if re.match("^[0-9]{2,3}$", id):
                    return id
                else:
                    logger.error("Enter valid id ")

        except ValueError:
            logger.error("Invalid input")
