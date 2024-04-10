import unittest 
import io
import sys
from list_functions import *

class TestListFunctions(unittest.TestCase):
    def test_compare_list_elements(self):
        # Test case 1: basic list=[10,20,30,20,10]
        result = compare_list_elements([10,20,30,20,10])
        self.assertTrue(result)

         # Test case 2: wrong list=[10,20,30,20,10]
        result = compare_list_elements([10,20,30,20,40])
        self.assertFalse(result)

         # Test case 3: 1 element list=[10,20,30,20,10]
        result = compare_list_elements([10])
        self.assertTrue(result)

    def test_print_divisible_by_five(self):
        # Test case 1: basic list=[10,20,30,20,10]
        result = get_divisible_by_five([10,29,38,20,10])
        self.assertEqual(result, [10,20,10])

        # Test case 2: no dividend of 5 list=[11,22,33,44]
        result = get_divisible_by_five([11,22,33,44])
        self.assertEqual(result, [])

         # Test case 3: empty list element list=[]
        result = get_divisible_by_five([])
        self.assertEqual(result, [])

    def test_merge_lists(self):
        # Test case 1: basic list1:[1, 2, 3, 4, 5], list2:[6, 7, 8, 9, 10]
        list1 = [1, 2, 3, 4, 5]
        list2 = [6, 7, 8, 9, 10]
        expected_output = [2, 4, 7, 9]
        self.assertEqual(merge_lists(list1, list2), expected_output)

        # Test case 1: empty lists list1:[], list2:[]
        list1 = []
        list2 = []
        expected_output = []
        self.assertEqual(merge_lists(list1, list2), expected_output)

if __name__ == '__main__':
    unittest.main()


