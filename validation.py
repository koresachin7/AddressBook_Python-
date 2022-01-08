import re
from loghandler import logger


class Validation:
    @staticmethod
    def validation(input_data, choice_key):
        """
            Description:
                         This method is used dictionary for validation
        """
        validation_dict = {"id": re.match("^[0-9]{2,3}$", input_data),
                           "name": re.match("^[A-Z]{1}[a-z]*$", input_data),
                           "mobile": re.match("^[7-9]{1}[0-9]{9}$", input_data),
                           "address": re.match("^[A-Z]{1}[a-z]+", input_data),
                           "zip": re.match("^[1-9]{1}[0-9]{5}$", input_data),
                           "city": re.match("^[A-Za-z]*$", input_data),
                           "state": re.match("^[A-Za-z]*$", input_data)}
        validation_data = validation_dict.get(choice_key)
        try:
            if validation_data:
                return input_data
            else:
                logger.error("name should be alphabets")
                print("plz Enter valida Input")

        except ValueError:
            logger.error("Invalid input")


