import unittest
from pprint import pprint
from Calculator import Calculator
from CSVFileReader import CSVFileReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_calculator_instantiation(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        self.calculator = Calculator()
        test_sub_data = CSVFileReader('/src/subtraction.csv').file_data
        for row in test_sub_data:
            self.assertEqual(self.calculator.subtract(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.value, int(row['Result']))





if __name__ == '__main__':
    unittest.main()
