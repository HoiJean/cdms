from commands.user import User
from constants import credentials
from constants.domaintypes import DomainTypes
from helpers.domainvalidation import DomainValidation
from screens.main import Main


class Login:

    def login_action(self):

        result = False
        while result is False:

            username = DomainValidation.validate_regex(DomainTypes.Username, 'Type your username', 'Username is incorrect')
            password = DomainValidation.accept_all('Type your password')
            result = User.login(username, password)
            if result is False:
                print('Please check your credentials')

        credentials.username = username
        main = Main.index_action()
