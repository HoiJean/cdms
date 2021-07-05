import csv
import os
from datetime import date, datetime


class Logger:
    filename = 'log.csv'
    fieldnames = ['No', 'Date', 'Time', 'Description of activity', 'Additional Information', 'Suspicious']
    file = None
    writer = None
    reader = None

    def __init__(self):
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
                'No': self.count_size(),
                'Date': current_date.strftime("%d-%m-%Y"),
                'Time': datetime.now().strftime("%H:%M:%S"),
                'Description of activity': description,
                'Additional Information': additional_information,
                'Suspicious': suspicious,
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
