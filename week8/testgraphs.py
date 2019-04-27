import unittest
from graphs import deep_find_all, deep_update

class TestDeepFindAll(unittest.TestCase):
    def test_if_a_dict_with_simple_values_like_int_gives_expected_answer(self):
        example_dict = {
        'a':3,
        'b':{
        'a':5
        }
        }
        expected_result = [3,5]
        self.assertEqual(deep_find_all(example_dict,'a'), expected_result)
    def test_if_a_key_which_is_a_dict_returns_the_result(self):
        example_dict2 = {
        'a':{
        'a1':3,
        'a2':5,
        'a3':6
        },
        'b':{
        'a':{
        'a4':'woohoo',
        'a5':'C'
        }
        }
        }
        expected_result2 = [{'a1':3,'a2':5,'a3':6},{'a4':'woohoo','a5':'C'}]
        self.assertEqual(deep_find_all(example_dict2,'a'), expected_result2)
class TestDeepUpdate(unittest.TestCase):
    def test_if_a_simple_dict_returns_expected_answer(self):
        example_dict = {
        'a':3,
        'b':{
        'a':5
        }
        }
        expected_dict = {
        'a':2,
        'b':{
        'a':2
        }
        }
        deep_find_all(example_dict,'a',2)
        self.assertEqual(example_dict, expected_result2)

if __name__ == '__main__':
    unittest.main()