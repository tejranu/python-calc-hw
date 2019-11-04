import unittest
from pprint import pprint
from Calculator import Calculator
from CSVFileReader import CSVFileReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_divide_method(self):
        div_data = CSVFileReader('/src/division.csv').file_data
        for row in div_data:
            self.assertEqual(self.calculator.divide(float(row['Value 1']), float(row['Value 2'])), float(row['Result']))
            self.assertEqual(self.calculator.value, round((row['Result'])), 10)


if __name__ == '__main__':
    unittest.main()
