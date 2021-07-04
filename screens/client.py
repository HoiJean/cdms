from commands.clientcommand import Clientcommand
from constants.domaintypes import DomainTypes
from helpers.consoleoutput import ConsoleOutput
from helpers.domainvalidation import DomainValidation
from helpers.typevalidation import TypeValidation


class Client:

	def __init__(self):
		self.command = Clientcommand()

	@staticmethod
	def show():
		return False

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


	@staticmethod
	def update():
		return False


	@staticmethod
	def delete():
		return False
