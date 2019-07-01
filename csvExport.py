# CSV file export
import csv

class csvExport:

    def __init__(self):
        self.file_name = ""

    def set_file_name(self,file_name):
        self.file_name = file_name

    def get_file_name(self):
        return self.file_name

    def write_to_csv(self,data):
        with open(self.file_name, "w", encoding='utf8') as file:
            output = csv.writer(file, delimiter=';')
            output.writerow(data[0].keys())
            for row in data:
                output.writerow(row.values())