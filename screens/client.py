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
            full_name = DomainValidation.validate(DomainTypes.full_name, 'Type the full name', ''
            'Fullname can only contain spaces and letters')
            street_address = DomainValidation.validate(DomainTypes.street_address, 'Type the street address',
            'Street cannot contain space at the begin or end and cannot contain a number')
            house_number = DomainValidation.validate(DomainTypes.house_number, 'Type the house number', ''
            'House number can contain numbers with optional added letter')
            zip_code = DomainValidation.validate(DomainTypes.zip_code, 'Type the zip code',
            'Zip code must be 4 numbers and 2 letters without a space')
            email = DomainValidation.validate(DomainTypes.email, 'Type the email', ''
            # Todo Add city list here
           'Email is incorrect')
            phone_number = DomainValidation.validate(DomainTypes.phone_number, 'Type the phone number', ''
            'Phone number is incorrect. Note: "+31 6" is already filled in')

            submitted = True

        return False

    @staticmethod
    def update():
        return False

    @staticmethod
    def delete():
        return False
