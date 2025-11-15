import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ➕ ADDITION TESTS
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, -4), -5)
        self.assertEqual(self.calc.add(-2, 5), 3)
        self.assertEqual(self.calc.add(0, 0), 0)

    # ➖ SUBTRACTION TESTS
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(-2, -5), 3)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    # ✖ MULTIPLICATION TESTS
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-3, 3), -9)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    # ➗ DIVISION TESTS
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, -3), -3)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    # Division by zero
    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == "__main__":
    unittest.main()
