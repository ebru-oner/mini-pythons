import unittest 
import io
import sys
from math_functions import *

class TestMathFunctions(unittest.TestCase):
    def test_calculate_sum_or_product(self):
        # Test case 1: product <= 1000
        result = calculate_sum_or_product(10,20)
        self.assertEqual(result, 200) 

        # Test case 2: product > 1000
        result = calculate_sum_or_product(100,20)
        self.assertEqual(result, 120) 

        # Test case 3: product = 1000
        result = calculate_sum_or_product(10,100)
        self.assertEqual(result, 1000) 

        # Test case 4: both numbers are 0
        result = calculate_sum_or_product(0,0)
        self.assertEqual(result, 0) 

        # Test case 5: one of the numbers is 0
        result = calculate_sum_or_product(0,20)
        self.assertEqual(result, 0) 

        # Test case 6: negative numbers
        result = calculate_sum_or_product(-70,-80)
        self.assertEqual(result, -150)

        # Test case 7: large numbers
        result = calculate_sum_or_product(10000,20000)
        self.assertEqual(result, 30000) 
        
        # Test case 8: Decimal numbers
        result = calculate_sum_or_product(10.8,20.6)
        self.assertEqual(result, 222.48000000000002) 

    def test_calculate_sum_of_current_and_previous(self):
        # Test case 1: basic, count = 1
        expected_output = "Current is: 1 previous is: 0 Sum is: 1\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        calculate_sum_of_current_and_previous(1)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output) 

        # Test case 2: zero, count = 0
        captured_output = io.StringIO()
        sys.stdout = captured_output
        calculate_sum_of_current_and_previous(0)
        sys.stdout = sys.__stdout__
        self.assertEqual(len(captured_output.getvalue()), 0) 

        # Test case 3: negative, count = -3
        result = calculate_sum_of_current_and_previous(-3)
        self.assertRaises(TypeError) 

    def test_is_palindrome(self):
        # Test case 1: palindrome, num:121
        result = is_palindrome(121)
        self.assertTrue(result)

        # Test case 2: not palindrome, num:123
        result = is_palindrome(1212)
        self.assertFalse(result)

        # Test case 3: negative palindrome, num:-121
        result = is_palindrome(-121)
        self.assertTrue(result)

        # Test case 4: 0 , num:0
        result = is_palindrome(0)
        self.assertTrue(result)

    def test_calculate_exponent(self):
        # Test case 1: base 2^3 = 8
        self.assertEqual(calculate_exponent(2, 3), 8) 

        # Test case 2: exponent zero 5^0 = 0
        self.assertEqual(calculate_exponent(5, 0), 1)  

        # Test case 3: base zero 0^5 = 0
        self.assertEqual(calculate_exponent(0, 5), 0)  

        # Test case 3: negative exponent 2^-2 
        self.assertAlmostEqual(calculate_exponent(2, -2), 0.25)  # 2^-2 = 1/4 = 0.25


if __name__ == '__main__':
    unittest.main()


