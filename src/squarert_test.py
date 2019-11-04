import unittest
from pprint import pprint
from Calculator import Calculator
from CSVFileReader import CSVFileReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_square_rt_method_test(self):
        sqrt_data = CSVFileReader('/src/squareroot.csv').file_data
        for row in sqrt_data:
            self.assertEqual(self.calculator.square_root(float((row['Value 1']))), float((row['Result'])))
            self.assertEqual(self.calculator.value, float((row['Result'])))


if __name__ == '__main__':
    unittest.main()
