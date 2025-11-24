import unittest
from main import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    # ------------------- ADD -------------------
    def test_add_integers(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(-3, -7), -10)

    def test_add_floats(self):
        self.assertAlmostEqual(add(2.5, 1.2), 3.7)
        self.assertAlmostEqual(add(-1.5, -2.5), -4.0)

    # ------------------- SUBTRACT -------------------
    def test_subtract_integers(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -7), 4)

    def test_subtract_floats(self):
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3)
        self.assertAlmostEqual(subtract(-1.5, -2.5), 1.0)

    # ------------------- MULTIPLY -------------------
    def test_multiply_integers(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-2, -3), 6)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 2), 5.0)
        self.assertAlmostEqual(multiply(-1.5, 2), -3.0)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(0, 0), 0)

    # ------------------- DIVIDE -------------------
    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_by_zero(self):
        self.assertEqual(divide(5, 0), "Error: Cannot divide by zero!")
        self.assertEqual(divide(0, 0), "Error: Cannot divide by zero!")

    def test_divide_floats(self):
        self.assertAlmostEqual(divide(2.5, 0.5), 5.0)
        self.assertAlmostEqual(divide(-2.5, 0.5), -5.0)


if __name__ == "__main__":
    unittest.main()
