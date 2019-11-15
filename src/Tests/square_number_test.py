import unittest
from pprint import pprint
from Calculator import Calculator
from CSVFileReader import CSVFileReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_square_method_test(self):
        square_data = CSVFileReader('/src/square.csv').file_data
        for row in square_data:
            self.assertEqual(self.calculator.square_number(int((row['Value 1']))), int((row['Result'])))
            self.assertEqual(self.calculator.value, int((row['Result'])))


if __name__ == '__main__':
    unittest.main()
