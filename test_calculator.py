import unittest
from calculator import Calculator
from multiply import multiplication

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        self.mul = multiplication()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)


    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(1, 1), 0)

    def test_multiply(self):
        self.assertEqual(self.mul.multiply(2, 2), 4)
        self.assertEqual(self.mul.multiply(1, 1), 1)

if __name__ == '__main__':
    unittest.main()