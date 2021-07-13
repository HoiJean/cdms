from datetime import date

from commands.advisorcommand import Advisorcommand
from commands.clientcommand import Clientcommand
from commands.passwordcommand import Passwordcommand
from commands.user import User
from constants import credentials
from constants.domaintypes import DomainTypes
from helpers import encryption
from helpers.consoleoutput import ConsoleOutput
from helpers.domainvalidation import DomainValidation
from helpers.logger import Logger
from helpers.typevalidation import TypeValidation
from screens import update_login_screen
from screens.update_login_screen import UpdateLoginScreen


class Advisor:

	def __init__(self):
		self.command = Advisorcommand()
		self.passwordCommand = Passwordcommand()
		self.logger = Logger()

	def show(self):
		result = self.command.get()
		clients = result.fetchall()

		crypter = encryption.Encryption()

		for client in clients:
			ConsoleOutput.success("------------------------")
			print("User ID: " + str(client['id']))
			print("Username: " + crypter.decrypt(client['username']))

			if client['full_name'] is not None:
				print("Fullname: " + client['full_name'])

			if client['registration_date'] is not None:
				print("Registration: " + client['registration_date'])

			if client['is_admin'] == 1:
				print("Role: system-admin")
			else:
				print("Role: advisor")
			ConsoleOutput.success("------------------------")

	def create(self, is_admin=0):

		username_validated = False
		username = ''
		while not username_validated:

			username = DomainValidation.validate(DomainTypes.Username, 'Type the username',
												 'Username can only contain letters, dashes, underscores, apostrophes, '
												 'periods',
												 min_length=5, max_length=20)
			username = str.lower(username)

			username_exists = self.command.get(username=username).fetchone()
			if username_exists is not None:
				ConsoleOutput.error('Username already exists...')
			else:
				username_validated = True

		full_name = DomainValidation.validate(DomainTypes.full_name, 'Type the full name',
											'full name can only contain letters, dashes and apostrophes',
											 min_length=5, max_length=20)

		valid_password = False
		password_first = ''

		while not valid_password:
			password_first = DomainValidation.validate(DomainTypes.password, 'Type your password', 'Password characters invalid')
			password_second = DomainValidation.validate(DomainTypes.password, 'Type your password', 'Password characters invalid')
			password_check = TypeValidation.is_strong_password(password_first)

			if password_first != password_second:
				ConsoleOutput.error('Passwords are not equal, please retype your password')
			elif password_check["password_ok"]:
				valid_password = True
			else:
				ConsoleOutput.error(
					"Password must be atleast 8 character, must have a combination of at least one lowercase letter, one uppercase letter, one digit, and one special character")

		crypter = encryption.Encryption()
		encryped_username = crypter.encrypt(username)
		self.command.create(
			username=encryped_username,
			full_name=full_name,
			registration_date=date.today(),
			password=self.passwordCommand.hash_password(password_first),
			is_admin=is_admin
		)

		if credentials.role > 0:
			ConsoleOutput.success('User created!')
			self.logger.write(credentials.username, 'New advisor is created', 'Username: ' + username, False)
		else:
			ConsoleOutput.success('Advisor created!')
			self.logger.write(credentials.username, 'New advisor is created', 'Username: ' + username, True)

	def create_admin(self):
		self.create(1)

	def update(self, update_type='username'):
		user_id = input('Which user ID do you want to edit?')
		if not TypeValidation.is_digit(user_id):
			ConsoleOutput.error('Please use a number')
		else:
			selected_user = self.command.get(id=user_id).fetchone()
			if selected_user is None:
				ConsoleOutput.error("Advisor not found")
			elif credentials.role != 2 and selected_user is not None and selected_user['is_admin']:
				ConsoleOutput.error('User is system admin, you are not authorized to do that')
			else:
				data = {}
				criteria = {'id': selected_user['id']}
				if update_type == 'password':
					# password_reset_screen = UpdateLoginScreen()
					# password_reset_screen.show(selected_user)
					raw_password = self.generate_password(8)
					encrypted_password = User.hash_password(raw_password)
					data = {
						'password': encrypted_password
					}
					self.command.update(criteria, data)

					print("Updated password")
					print("Temporary password: " + raw_password)
					print()
				else:
					username = DomainValidation.validateOptionalFields(DomainTypes.Username, 'Type the username',
																	   'Username can only contain letters, dashes, underscores, apostrophes, '
																	   'periods')
					if not username:
						username = selected_user['username']

					crypter = encryption.Encryption()
					encrypted_username = crypter.encrypt(username)
					data = {
						'username': encrypted_username,
					}

					if credentials.role > 0:
						self.logger.write(credentials.username, 'Advisor is updated', 'Username: ' + username, False)
					else:
						self.logger.write(credentials.username, 'Advisor is updated', 'Username: ' + username, True)

					self.command.update(criteria, data)
					ConsoleOutput.success('Advisor has been updated.')

	def update_password(self):
		self.update('password')

	def delete(self):
		user_id = input('Which user ID do you want to delete?')
		if not TypeValidation.is_digit(user_id):
			ConsoleOutput.error('Please use a number')
		else:
			selected_user = self.command.get(id=user_id).fetchone()
			if selected_user is None:
				ConsoleOutput.error("Advisor not found")
			elif selected_user is not None and selected_user['is_admin'] == 1 and credentials.role != 2:
				ConsoleOutput.error('User is system admin, you are not authorized to do that')
			else:
				self.command.remove(id=selected_user['id'])
				ConsoleOutput.success('Advisor has been deleted')
				if credentials.role == 1:
					self.logger.write(credentials.username, 'Advisor is removed',
									  'Username: ' + selected_user['username'], False)
				else:
					self.logger.write(credentials.username, 'New advisor is removed',
									  'Username: ' + selected_user['username'], True)

	def generate_password(self, length):
		if not isinstance(length, int) or length < 8:
			raise ValueError("temp password must have positive length")

		chars = "234679ADEFGHJKLMNPRTUWabdefghijkmnpqrstuwy"
		from os import urandom

		return "".join(chars[c % len(chars)] for c in urandom(length))

