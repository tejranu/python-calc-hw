import csv


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:
    file_data = []

    def __init__(self, filepath):
        with open(absolutepath(filepath)) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.file_data.append(row)
        pass

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.file_data:
            objects.append(ClassFactory(class_name, row))
        return objects