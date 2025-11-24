import unittest

# Import functions from your calculator code
# If your calculator code is in calculator.py, use:
# from calculator import add, subtract, multiply, divide

# For demonstration purposes I re-define them here:
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 5), 4)
        self.assertAlmostEqual(add(2.5, 1.2), 3.7)

    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(0, 5), -5)
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertAlmostEqual(multiply(2.5, 2), 5.0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)

        # division by zero
        self.assertEqual(divide(5, 0), "Error: Cannot divide by zero!")

    def test_divide_negative(self):
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)


if __name__ == "__main__":
    unittest.main()
