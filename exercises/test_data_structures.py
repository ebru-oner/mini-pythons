import unittest 
from data_structures import *

class TestDataStructures(unittest.TestCase):
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

    def test_(self):
        # Test case 1: basic
        a_list = [1, 2, 3, 4, 5]
        remove_index = 2
        add_index = 0
        expected_result = [3, 1, 2, 4, 5,3]
        result = remove_add_item_in_list(a_list, remove_index, add_index)
        self.assertEqual(result, expected_result)

        # Test case 2: index out of range
        a_list = [1, 2, 3, 4, 5]
        remove_index = 10
        add_index = 0
        result = remove_add_item_in_list(a_list, remove_index, add_index)
        self.assertIsNone(result)

        # Test case 3: empty
        remove_index = 10
        add_index = 0
        result = remove_add_item_in_list([], remove_index, add_index)
        self.assertIsNone(result)

    def test_slice_and_reverse(self):
        # Test case 1: basic 
        result = slice_and_reverse([1,2,3,4,5,6,7,8,9])
        self.assertListEqual(result, [[3,2,1],[6,5,4],[9,8,7]])

        # Test case 2: empty 
        result = slice_and_reverse([])
        self.assertIsNone(result)

        # Test case 3: not divisible by 3 
        result = slice_and_reverse([0,1,2,3,4,5,6,7,8,9])
        self.assertListEqual(result, [[3,2,1,0],[7,6,5,4],[9,8]])

    def test_pair_lists(self):
        # Test case 1: basic 
        result = pair_lists([1,2,3],[5,6,7])
        self.assertListEqual(result, [(1,5), (2,6),(3,7)])

        # Test case 2: both empty 
        result = pair_lists([],[])
        self.assertIsNone(result)

        # Test case 3: second list empty 
        result = pair_lists([1,2,3],[])
        self.assertIsNone(result)

        # Test case 4: first list empty 
        result = pair_lists([], [1,2,3])
        self.assertIsNone(result)

    def test_intersection_of_sets(self):
        # Test case 1: has intersection 
        set_1 = {1,2,3,4,5}
        set_2 = {4,5,6,7,8}
        expected_result_1 = {1,2,3}
        result_1, result_2 = intersection_of_sets(set_1,set_2)
        self.assertEqual(result_1, expected_result_1)
        self.assertEqual(result_2, set_2)


        # Test case 2: no intersection 
        set_1 = {1,2,3,4,5}
        set_2 = {4,5,6,7,8}
        result_1, result_2 = intersection_of_sets(set_1,set_2)
        self.assertEqual(result_1, set_1)
        self.assertEqual(result_2, set_2)

        # Test case 3: empty lists 
        result_1, result_2 = intersection_of_sets(set(),set())
        self.assertSetEqual(result_1, set())
        self.assertSetEqual(result_2, set())

    def test_clear_subset(self):
        # Test case 1: set_1 subset of set_2
        set_1 = {4,5}
        set_2 = {4,5,6,7,8}
        expected_result_1 = set()
        result_1, result_2 = clear_subset(set_1,set_2)
        self.assertEqual(result_1, expected_result_1)
        self.assertEqual(result_2, set_2)


        # Test case 2: set_1 superset of set_2 
        set_1 = {1,2,3,4,5}
        set_2 = {4,5}
        result_1, result_2 = clear_subset(set_1,set_2)
        expected_result_2 = set()
        self.assertEqual(result_1, set_1)
        self.assertEqual(result_2, expected_result_2)

        # Test case 3: set_1 not superset of set_2 
        set_1 = {1,2,3,4,5}
        set_2 = {4,5,9}
        result_1, result_2 = clear_subset(set_1,set_2)
        self.assertEqual(result_1, set_1)
        self.assertEqual(result_2, set_2)


if __name__ == '__main__':
    unittest.main()


