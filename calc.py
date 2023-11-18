import unittest

class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        # Creating an instance of the Calculator class before each test
        self.calc = Calculator()

    def test_add(self):
        # Testing the add method of the Calculator class
        self.assertEqual(11, self.calc.add(3, 7), "The addition is wrong")

    def test_subtract(self):
        # Testing the subtract method of the Calculator class
        self.assertEqual(12, self.calc.subtract(15, 3), "Subtraction is wrong")
        self.assertEqual(10, self.calc.subtract(15, 3), "Subtraction is wrong")

    def test_multiply(self):
        # Testing the multiply method of the Calculator class
        self.assertEqual(30, self.calc.multiply(5, 6), "Multiplication is wrong")
        self.assertEqual(20, self.calc.multiply(5, 6), "Multiplication is wrong")

    def test_divide(self):
        # Testing the divide method of the Calculator class
        self.assertEqual(3, self.calc.divide(6, 2), "Division is wrong")
        
        # Testing division with incorrect expected result
        self.assertEqual(3, self.calc.divide(6, 2), "Division is wrong")
        self.assertEqual(2, self.calc.divide(8, 4), "Division is wrong")

# Entry point for running the tests
if __name__ == '__main__':
    unittest.main()
