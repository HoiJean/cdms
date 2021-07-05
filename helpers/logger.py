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

    def write(self, description, additional_information, suspicious=False):
        self.open()

        current_date = datetime.now()

        suspicious = 'No'
        if suspicious is True:
            suspicious = 'Yes'

        self.writer.writerow(
            {
                self.encryption.encrypt('No'): self.encryption.encrypt(self.count_size()),
                self.encryption.encrypt('Date'): self.encryption.encrypt(current_date.strftime("%d-%m-%Y")),
                self.encryption.encrypt('Time'): self.encryption.encrypt(datetime.now().strftime("%H:%M:%S")),
                self.encryption.encrypt('Description of activity'): self.encryption.encrypt(description),
                self.encryption.encrypt('Additional Information'): self.encryption.encrypt(additional_information),
                self.encryption.encrypt('Suspicious'): self.encryption.encrypt(suspicious),
            })

        self.close()

    def open(self):
        self.file = open(self.filename, mode='r+')
        self.reader = csv.reader(self.file)
        self.writer = csv.DictWriter(self.file, fieldnames=self.fieldnames)

    def close(self):
        self.file.close()
        self.reader = None
        self.writer = None

    def count_size(self):
        length = 0
        try:
            length = len(list(self.reader))
        except:
            print('error occurred fetching logging file')

        return length
