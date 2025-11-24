# src/test_main.py

import unittest
from main import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    # ------------------- ADD -------------------
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 5), 4)
        self.assertAlmostEqual(add(2.5, 1.2), 3.7)

    # ------------------- SUBTRACT -------------------
    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(0, 5), -5)
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3)

    # ------------------- MULTIPLY -------------------
    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertAlmostEqual(multiply(2.5, 2), 5.0)
        self.assertEqual(multiply(5, 0), 0)

    # ------------------- DIVIDE -------------------
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_by_zero(self):
        self.assertEqual(divide(5, 0), "Error: Cannot divide by zero!")
        self.assertEqual(divide(0, 0), "Error: Cannot divide by zero!")

if __name__ == "__main__":
    unittest.main()
