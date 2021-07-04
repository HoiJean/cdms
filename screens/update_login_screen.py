from commands.user import User
from helpers.consoleoutput import ConsoleOutput
from helpers.typevalidation import TypeValidation


class UpdateLoginScreen:

	def show(self):
		valid = False

		while not valid:
			new_password = input('Enter a new password: ')
			new_password_confirm = input('Re-enter a new password: ')

			if new_password == new_password_confirm:
				password_check = TypeValidation.is_strong_password(new_password)
				if password_check["password_ok"]:
					valid = True
					print("Updating login...")
					user = User()
					user.update_password(new_password)
					ConsoleOutput.success("Updated your password")
				else:
					print("Password must be atleast 8 character, must have a combination of at least one lowercase letter, one uppercase letter, one digit, and one special character")
			else:
				ConsoleOutput.error('Password confirm did not match.')
