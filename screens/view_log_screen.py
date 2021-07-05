from helpers.encryption import Encryption
from helpers.logger import Logger


class ViewLogScreen:

    def show(self):
        encrypt = Encryption()
        log = Logger()

        line_count = 0
        all_columns = ""

        log_data = log.read()

        for row in log_data:
            for key in row:
                all_columns += "    " + encrypt.decrypt(key) + "    |"

            if line_count == 0:
                print(all_columns)
                line_count += 1
            print(
                f'{encrypt.decrypt(row[encrypt.encrypt("No")])} {encrypt.decrypt(row[encrypt.encrypt("Username")])} {encrypt.decrypt(row[encrypt.encrypt("Date")])} {encrypt.decrypt(row[encrypt.encrypt("Time")])} {encrypt.decrypt(row[encrypt.encrypt("Description of activity")])} {encrypt.decrypt(row[encrypt.encrypt("Additional Information")])} {encrypt.decrypt(row[encrypt.encrypt("Suspicious")])}')
            line_count += 1
        print(f'Processed {line_count} lines.')
