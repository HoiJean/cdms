from commands.advisorcommand import Advisorcommand
from commands.clientcommand import Clientcommand
from commands.passwordcommand import Passwordcommand
from constants.domaintypes import DomainTypes
from helpers.consoleoutput import ConsoleOutput
from helpers.domainvalidation import DomainValidation
from helpers.typevalidation import TypeValidation


class Advisor:

    def __init__(self):
        self.command = Advisorcommand()
        self.passwordCommand = Passwordcommand()

    def show(self):
        pass

    def create(self):

        username_validated = False
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

        valid_password = False
        password_first = ''

        while not valid_password:
            password_first = DomainValidation.accept_all('Type the password')
            password_second = DomainValidation.accept_all('Confirm the password')
            password_check = TypeValidation.is_strong_password(password_first)

            if password_first != password_second:
                ConsoleOutput.error('Passwords are not equal, please retype your password')
            elif password_check["password_ok"]:
                valid_password = True
            else:
                ConsoleOutput.error(
                    "Password must be atleast 8 character, must have a combination of at least one lowercase letter, one uppercase letter, one digit, and one special character")

        self.command.create(
            username=username,
            password=self.passwordCommand.hash_password(password_first),
            is_admin=0
        )

        ConsoleOutput.success('Advisor created!')

    pass

    def update(self):
        pass

    def delete(self):
        pass
