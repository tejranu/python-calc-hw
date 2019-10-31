import csv
from pprint import pprint


def build(class_name, dict_name):
    return type(class_name, (object,), dict_name)


class CSVFileReader:
    file_data = []

    def __init__(self, csvfile):
        # when constructor is created
        # open the file
        with open(csvfile) as data:
            csv_data = csv.DictReader(data, delimiter=",")
            # seperate each value from the csv file by comma found

            for row in csv_data:
                self.file_data.append(row)
        pass


    def return_data(self, class_name):
        objects = []
        for row in self.data:
            objects.append(build(class_name, row))
        return objects