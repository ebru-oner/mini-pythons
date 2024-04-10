import unittest 
import io
import sys
from string_functions import *

class TestMathFunctions(unittest.TestCase):
    def test_print_chars_at_even_index(self):
        # Test case 1: basic string = "even"
        expected_output = "e\ne\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_chars_at_even_index("even")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output) 

        # Test case 2: no string string = ""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_chars_at_even_index("")
        sys.stdout = sys.__stdout__
        self.assertEqual(len(captured_output.getvalue()), 0) 

        # Test case 3: 1 char string string = "e\n"
        expected_output = "e\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_chars_at_even_index("e")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output) 

    def test_remove_first_n_chars_1(self):
        # Test case 1: basic string:"pppython", count:2
        result = remove_first_n_chars("pppython", 2)
        self.assertEqual(result, "python")
        
        # Test case 2: no string:"", count:2
        result = remove_first_n_chars("", 2)
        self.assertEqual(result, None)
        
        # Test case 3: count > len(str) string:"python", count:10
        result = remove_first_n_chars("python", 10)
        self.assertEqual(result, None)

    def test_count_substring(self):
        # Test case 1: basic string:"me and you and he and she", substr:"and"
        result = count_substring("me and you and he and she", "and")
        self.assertEqual(result, 3)

        # Test case 2: no substr present string:"me and you and he and she", substr:"they"
        result = count_substring("me and you and he and she", "they")
        self.assertEqual(result, 0)

    def test_get_first_middle_last(self):
        # Test case 1: basic string:python
        result = get_first_middle_last("python")
        self.assertEqual(result, "phn")

        # Test case 2: 1 char string:p
        result = get_first_middle_last("p")
        self.assertEqual(result, "p")

    def test_get_get_middle_three_chars(self):
        # Test case 1: basic string:python
        result = get_middle_three_chars("python")
        self.assertEqual(result, "tho")

        # Test case 2: 1 char string:p
        result = get_middle_three_chars("p")
        self.assertEqual(result, None)
        
        
if __name__ == '__main__':
    unittest.main()


