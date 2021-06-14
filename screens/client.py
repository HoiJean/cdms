from constants.domaintypes import DomainTypes
from helpers.domainvalidation import DomainValidation


class Client:

    @staticmethod
    def show():
        return False

    @staticmethod
    def create():
        submitted = False
        while not submitted:
            full_name = DomainValidation.validate(DomainTypes.full_name, 'Type the full name', '')
            street_address = DomainValidation.validate(DomainTypes.street_address, 'Type the street address', '')
            house_number = DomainValidation.validate(DomainTypes.house_number, 'Type the house number', '')
            zip_code = DomainValidation.validate(DomainTypes.zip_code, 'Type the zip code', '')
            email = DomainValidation.validate(DomainTypes.email, 'Type the email', '')
            phone_number = DomainValidation.validate(DomainTypes.phone_number, 'Type the phone number', '')

            submitted = True

        return False

    @staticmethod
    def update():
        return False

    @staticmethod
    def delete():
        return False
