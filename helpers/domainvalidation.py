import re


class DomainValidation:

    @staticmethod
    def validate(validation_type, message_name, error_output):
        validated = None
        while not validated:
            user_input = input(message_name)
            if not re.match(validation_type, user_input):
                print(error_output)
            else:
                return user_input

    @staticmethod
    def accept_all(message_name):
        user_input = input(message_name)
        return user_input
