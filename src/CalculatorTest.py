import unittest
from pprint import pprint
from Calculator import Calculator
from CSVFileReader import CSVFileReader


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_calculator_instantiation(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_add_data = CSVFileReader('/src/')




if __name__ == '__main__':
    unittest.main()
