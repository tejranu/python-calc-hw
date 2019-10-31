import unittest
from pprint import pprint
from Calculator import Calculator
from CSVFileReader import CSVFileReader


class CalculatorInstantiationCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
        
    def test_calculator_instantiation(self):
        self.assertIsInstance(self.calculator, Calculator)
        

class SubtractCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_calculator_instantiation(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        self.calculator = Calculator()
        test_data = CSVFileReader('/src/subtraction.csv').file_data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.value, int(row['Result']))
        test_data = []


class AddCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_calculator_instantiation(self):
        self.assertIsInstance(self.calculator, Calculator)

    def add_method_test(self):
        add_data = CSVFileReader('/src/addition.csv').file_data
        for row in add_data:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.value, int(row['Result']))


class MultiplyCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_calculator_instantiation(self):
        self.assertIsInstance(self.calculator, Calculator)

    def multiply_method_test(self):
        mult_data = CSVFileReader('/src/multiply.csv').file_data
        for row in mult_data:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.value, int(row['Result']))


class DivideCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def divide_method_test(self):
        div_data = CSVFileReader('/src/division.csv').file_data
        for row in div_data:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.value, int(row['Result']))



if __name__ == '__main__':
    unittest.main()
