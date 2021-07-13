import csv
import os
from datetime import date, datetime

from helpers.encryption import Encryption


class Logger:
    filename = 'log.csv'
    fieldnames = None
    file = None
    writer = None
    reader = None
    encryption = None

    def __init__(self):
        self.encryption = Encryption()

        self.fieldnames = [
            self.encryption.encrypt('No'),
            self.encryption.encrypt('Username'),
            self.encryption.encrypt('Date'),
            self.encryption.encrypt('Time'),
            self.encryption.encrypt('Description of activity'),
            self.encryption.encrypt('Additional Information'),
            self.encryption.encrypt('Suspicious')
        ]

        file_exists = os.path.isfile(self.filename)
        if file_exists is False:
            file = open(self.filename, mode='w')
            self.writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            self.writer.writeheader()
            file.close()

    def write(self, username, description, additional_information, suspicious=False):
        try:
            self.open()

            current_date = datetime.now()

            if suspicious is True:
                suspicious = 'Yes'
            else:
                suspicious = 'No'

            self.writer.writerow(
                {
                    self.encryption.encrypt('No'): self.count_size(),
                    self.encryption.encrypt('Username'): self.encryption.encrypt(username),
                    self.encryption.encrypt('Date'): current_date.strftime("%d-%m-%Y"),
                    self.encryption.encrypt('Time'): datetime.now().strftime("%H:%M:%S"),
                    self.encryption.encrypt('Description of activity'): self.encryption.encrypt(description),
                    self.encryption.encrypt('Additional Information'): self.encryption.encrypt(additional_information),
                    self.encryption.encrypt('Suspicious'): self.encryption.encrypt(suspicious),
                })
            self.close()
        except Exception as e:
            print('Log file corrupted, error writing file')

    def read(self):
        try:
            self.open()
            data = list(self.reader)
            self.close()
            return data
        except Exception as e:
            print('Log file corrupted, error reading file')


    def open(self):
        try:
            self.file = open(self.filename, mode='r+')
            self.reader = csv.DictReader(self.file)
            self.writer = csv.DictWriter(self.file, fieldnames=self.fieldnames)
        except Exception as e:
            print('Log file corrupted, error opening file')

    def close(self):
        try:
            self.file.close()
            self.reader = None
            self.writer = None
        except Exception as e:
            print('Log file corrupted, error closing file')

    def count_size(self):
        length = 0
        try:
            length = len(list(self.reader))
            return length
        except Exception as e:
            print('Log file corrupted, error counting file file')

