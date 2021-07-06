from commands.user import User
from constants import credentials
from constants.domaintypes import DomainTypes
from helpers.domainvalidation import DomainValidation
from helpers.logger import Logger
from screens.main import Main


class Login:

	def login_action(self):

		log = Logger()

		result = False

		while result is False:
			user_obj = User()
			username = DomainValidation.validate(DomainTypes.Username, 'Type your username', 'Username characters are incorrect')
			password = DomainValidation.accept_all('Type your password')

			result = user_obj.login(username, password)

			if username == credentials.superadmin and password == credentials.superadmin_password:
				credentials.username = username
				credentials.role = 2
				result = True
			else:
				if result is False:
					log.write(username, 'Login failed', f'Username { username} is used with password { password}', True)
					print('Please check your credentials')
				else:
					credentials.username = result["username"]
					credentials.role = result["is_admin"]

		Main.index_action()
