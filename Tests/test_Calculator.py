import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        calculator = Calculator()
        result = 4
        self.assertEqual(calculator.add(2, 2), result)
        self.assertEqual(calculator.result, result)

    def test_add_method_calculatorCSV(self):
        calculator = Calculator()
        test_data = CsvReader('Data/Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(calculator.result, result)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        result = 0
        self.assertEqual(calculator.subtract(2, 2), result)
        self.assertEqual(calculator.result, result)

    def test_subtract_method_calculatorCSV(self):
        calculator = Calculator()
        test_data = CsvReader('Data/Subtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(calculator.result, result)

    def test_multiply_method_calculator(self):
        calculator = Calculator()
        result = 4
        self.assertEqual(calculator.multiply(2, 2), result)
        self.assertEqual(calculator.result, result)

    def test_multiply_method_calculatorCSV(self):
        calculator = Calculator()
        test_data = CsvReader('Data/Multiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(calculator.result, result)


if __name__ == '__main__':
    unittest.main()
