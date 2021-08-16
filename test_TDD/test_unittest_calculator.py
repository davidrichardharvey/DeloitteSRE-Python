from calculator import SimpleCalculator
from unittest import TestCase

class CalculatorTests(TestCase):
    calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 7), 9)
        self.assertEqual(self.calc.add(-5, -20), -25)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 7), -5)
        self.assertEqual(self.calc.subtract(-5, -20), 15)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 7), 14)
        self.assertEqual(self.calc.multiply(3453, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(8, 4), 2.0)


