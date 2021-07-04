from commands.clientcommand import Clientcommand
from constants.domaintypes import DomainTypes
from helpers.consoleoutput import ConsoleOutput
from helpers.domainvalidation import DomainValidation
from helpers.typevalidation import TypeValidation


class Client:

    def __init__(self):
        self.command = Clientcommand()

    def show(self):
        full_name = DomainValidation.validate(DomainTypes.full_name, 'Type the full name', '')
        result = self.command.search(full_name)
        clients = result.fetchall()

        for client in clients:
            ConsoleOutput.success("------------------------")
            print("Client ID: " + str(client['id']))
            print("Full Name: " + client['full_name'])
            print("Street: " + client['street_name'])
            print("House number: " + client['house_number'])
            print("Zip code: " + client['zip_code'])
            print("City: " + client['city'])
            print("Email: " + client['email'])
            print("Phone: " + client['phone_number'])
            ConsoleOutput.success("------------------------")

    def create(self):
        submitted = False
        full_name = ""
        street_name = ""
        house_number = ""
        zip_code = ""
        email = ""
        phone_number = ""
        city = ""
        while not submitted:
            full_name = DomainValidation.validate(DomainTypes.full_name, 'Type the full name', '')
            street_name = DomainValidation.validate(DomainTypes.street_address, 'Type the street address', '')
            house_number = DomainValidation.validate(DomainTypes.house_number, 'Type the house number', '')
            zip_code = DomainValidation.validate(DomainTypes.zip_code, 'Type the zip code', '')
            email = DomainValidation.validate(DomainTypes.email, 'Type the email', '')
            phone_number = DomainValidation.validate(DomainTypes.phone_number, 'Type the phone number', '')

            city_validated = None
            while not city_validated:
                print('1: Amsterdam')
                print('2: Rotterdam')
                print('3: Den-Haag')
                print('4: Schiedam')
                print('5: Breda')
                print('6: Utrecht')
                print('7: Eindhoven')
                print('8: Tilburg')
                print('9: Almere')
                print('10: Groningen')
                city = input('Type number to select city')
                if not TypeValidation.is_digit(city):
                    ConsoleOutput.error("Please use a number")
                else:
                    city = int(city)
                    if city > 10 or city < 1:
                        ConsoleOutput.error("Please select a correct city number")
                    else:
                        if city == 1:
                            city = 'Amsterdam'
                        elif city == 2:
                            city = 'Rotterdam'
                        elif city == 3:
                            city = 'Den-Haag'
                        elif city == 4:
                            city = 'Schiedam'
                        elif city == 5:
                            city = 'Breda'
                        elif city == 6:
                            city = 'Utrecht'
                        elif city == 7:
                            city = 'Eindhoven'
                        elif city == 8:
                            city = 'Tilburg'
                        elif city == 9:
                            city = 'Almere'
                        elif city == 10:
                            city = 'Groningen'
                        city_validated = True

            submitted = True

        self.command.create(
            full_name=full_name,
            street_name=street_name,
            house_number=house_number,
            zip_code=zip_code,
            email=email,
            phone_number=phone_number,
            city=city
        )

        return True

    def update(self):

        client_id = input('Which client ID do you want to edit?')
        if not TypeValidation.is_digit(client_id):
            ConsoleOutput.error('Please use a number')
        else:
            selected_client = self.command.get(id=client_id).fetchone()

            full_name = DomainValidation.validateOptionalFields(DomainTypes.full_name, 'Type the full name', '')
            street_name = DomainValidation.validateOptionalFields(DomainTypes.street_address, 'Type the street address',
                                                                  '')
            house_number = DomainValidation.validateOptionalFields(DomainTypes.house_number, 'Type the house number',
                                                                   '')
            zip_code = DomainValidation.validateOptionalFields(DomainTypes.zip_code, 'Type the zip code', '')
            email = DomainValidation.validateOptionalFields(DomainTypes.email, 'Type the email', '')
            phone_number = DomainValidation.validateOptionalFields(DomainTypes.phone_number, 'Type the phone number',
                                                                   '')

            city_validated = None
            while not city_validated:
                print('1: Amsterdam')
                print('2: Rotterdam')
                print('3: Den-Haag')
                print('4: Schiedam')
                print('5: Breda')
                print('6: Utrecht')
                print('7: Eindhoven')
                print('8: Tilburg')
                print('9: Almere')
                print('10: Groningen')
                print("0: Don't change the city!")
                city = input('Type number to select city')
                if not TypeValidation.is_digit(city):
                    ConsoleOutput.error("Please use a number")
                else:
                    city = int(city)
                    if city > 10 or city < 0:
                        ConsoleOutput.error("Please select a correct city number")
                    else:
                        if city == 1:
                            city = 'Amsterdam'
                        elif city == 2:
                            city = 'Rotterdam'
                        elif city == 3:
                            city = 'Den-Haag'
                        elif city == 4:
                            city = 'Schiedam'
                        elif city == 5:
                            city = 'Breda'
                        elif city == 6:
                            city = 'Utrecht'
                        elif city == 7:
                            city = 'Eindhoven'
                        elif city == 8:
                            city = 'Tilburg'
                        elif city == 9:
                            city = 'Almere'
                        elif city == 10:
                            city = 'Groningen'
                        elif city == 0:
                            city = False
                        city_validated = True


            print(full_name)
            if not full_name:
                full_name = selected_client['full_name']
            if not street_name:
                street_name = selected_client['street_name']
            if not house_number:
                house_number = selected_client['house_number']
            if not zip_code:
                zip_code = selected_client['zip_code']
            if not email:
                email = selected_client['email']
            if not phone_number:
                phone_number = selected_client['phone_number']
            if not city:
                city = selected_client['city']


            criteria = {'id': selected_client['id']}
            data = {
                'full_name': full_name,
                'street_name': street_name,
                'house_number': house_number,
                'zip_code': zip_code,
                'email': email,
                'phone_number': phone_number,
                'city': city
            }

            self.command.update(criteria, data)


        @staticmethod
        def delete():
            return False
