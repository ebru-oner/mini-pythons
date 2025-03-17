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

    def test_create_combination_of_strings(self):
        # Test case 1: basic list:["multiple","strings"]
        result = create_combination_of_strings(["multiple", "strings"])
        self.assertEqual(result, "miesis") 

        # Test case 2: empty list:[]
        result = create_combination_of_strings([])
        self.assertEqual(len(result), 0) 
    
    def test_make_lowercases_prefix(self):
        # Test case 1: basic str:"HelLo"
        result = make_lowercases_prefix("HelLo")
        self.assertEqual(result, "eloHL")

        # Test case 2: empty str:""
        result = make_lowercases_prefix("")
        self.assertEqual(len(result), 0) 

    def test_group_characters_in_string(self):
        # Test case 1: a string with all str: @#$123qwe
        result = group_characters_in_string("@12qwe")
        self.assertEqual(result, "@12qwe has 3 chars 2 digits 1 symbols.")

        # Test case 2: empoty string str: ""
        result = group_characters_in_string("")
        self.assertEqual(result, " has 0 chars 0 digits 0 symbols.")
    
    def test_is_balanced_string(self):
        # Test case 1: balanced string with all str1: this string, str2:is in this string
        result = is_balanced_string("this string", "is in this string")
        self.assertTrue(result)

        # Test case 2: not balanced str1: this string, str2:is not in this
        result = is_balanced_string("this string","is not in this")
        self.assertFalse(result)

    def test_count_char_occurrences(self):
        # Test case 1: empty str:""
        result = count_char_occurrences("")
        self.assertEqual(result, {})

        # Test case 2: multiple occurences str:ewrbDDDerweee
        result = count_char_occurrences("ewrbDDDerweee")
        self.assertEqual(len(result), 5)

    def test_reverse_string(self):
        # Test case 1:  empty str=""
        result = reverse_string("")
        self.assertEqual(result, "")

        # Test case 2:  basic str="string"
        result = reverse_string("string")
        self.assertEqual(result, "gnirts")

    def test_remove_empty_strings(self):
        # Test case 1: list with empty str, list:["ww","",None,"","dd"]
        result = remove_empty_strings(["ww","",None,"","dd"])
        self.assertEqual(result, ["ww","dd"])

        # Test case 2: empty list list:[]
        result = remove_empty_strings([])
        self.assertEqual(result, [])

    def test_remove_characters_keep_integer(self):
        # Test case 1: string  with numbers str:"qw 23 dw ddw 55"
        result = remove_characters_keep_integers("qw 23 dw ddw 55")
        self.assertEqual(result, "2355")

        # Test case 2: string  with numbers within str str:"qw23 dw ddw 55"
        result = remove_characters_keep_integers("qw23 dw ddw 55")
        self.assertEqual(result, "2355")

        # Test case 3: empty str:""
        result = remove_characters_keep_integers("")
        self.assertEqual(result, "")

    def test_find_combination_of_alphabets_numbers(self):
        # Test case 1: string contains alphanumeric str:"str1 string in the3"
        result = find_combination_of_alphabets_numbers("str1 string in the3")
        self.assertEqual(result, ["str1", "the3"])

        # Test case 2: string contains alphanumeric and number str:"str1 string in the3 33"
        result = find_combination_of_alphabets_numbers("str1 string in the3 33")
        self.assertEqual(result, ["str1", "the3"])

        # Test case 3: string contains no alphanumeric str:"str string in the"
        result = find_combination_of_alphabets_numbers("str string in the 33")
        self.assertEqual(len(result), 0)

        # Test case 4: empty str:""
        result = find_combination_of_alphabets_numbers("")
        self.assertEqual(len(result), 0)

    def test_replace_symbols(self):
        # Test case 1: basic str: $tring w!th speci@l chara&cters
        result = replace_symbols("$tring w!th speci@l chara&cters","#")
        self.assertEqual(result, "#tring w#th speci#l chara#cters")

        # Test case 2: no special char str: String with special characters
        result = replace_symbols("String with special characters","#")
        self.assertEqual(result, "String with special characters")

        # Test case 3: empty str: ""
        result = replace_symbols("","#")
        self.assertEqual(result, "")

        
if __name__ == '__main__':
    unittest.main()


