class TypeValidation:

    @staticmethod
    def is_digit(check_input):
        '''
        function checking if your string is a pure digit, int
        return : bool
        '''
        if check_input.isdigit():
            return True
        return False

    @staticmethod
    def is_string_only(check_input):
        '''
        function checking if your string is all letters
        return : bool
        '''
        if check_input.isalpha():
            return True
        return False

    @staticmethod
    def is_string_with_space(check_input):
        '''
        function checking if your string is all letters, but including space(s)
        return : bool
        '''
        valid = False
        if ' ' in check_input:
            for char in check_input:
                if char.isdigit():
                    valid = False
                elif char.isalpha() or char.isspace():
                    valid = True
        return valid

    @staticmethod
    def is_string_or_num(check_input):
        '''
        function checking if your string is all letters or numbers
        return : bool
        '''
        if check_input.isalnum():
            return True
        return False

    @staticmethod
    def is_float(check_input):
        '''
        function checking if your string is a floating point
        return : bool
        '''
        if '.' in check_input:
            split_number = check_input.split('.')
            if len(split_number) == 2 and split_number[0].isdigit() and split_number[1].isdigit():
                return True
        return False