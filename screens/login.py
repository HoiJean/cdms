from commands.user import User
from constants import credentials
from constants.domaintypes import DomainTypes
from helpers.domainvalidation import DomainValidation
from screens.main import Main


class Login:

	def login_action(self):

		result = False

		while result is False:
			user_obj = User()
			username = DomainValidation.validate(DomainTypes.Username, 'Type your username', 'Username is incorrect')
			password = DomainValidation.accept_all('Type your password')

			result = user_obj.login(username, password)

			if result is False:
				print('Please check your credentials')
			else:
				credentials.username = result["username"]
				credentials.role = result["is_admin"]

		Main.index_action()
