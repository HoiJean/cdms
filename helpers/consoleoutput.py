from helpers.color import Color


class ConsoleOutput:

    @staticmethod
    def error(message):
        print(Color.FAIL + message + Color.ENDC)

    @staticmethod
    def success(message):
        print(Color.OKGREEN + message + Color.ENDC)
