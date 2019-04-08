import unittest

from decorators import accepts, say_my_name, encrypt, get_string

class TestTheAccepts(unittest.TestCase):
    def test_if_a_int_returns_the_typeerror(self):
        random_int = 'ha'
        self.assertRaises(TypeError, say_my_name(random_int))
    def test_if_a_one_variable_function_passes_when_its_passed_on_correctly(self):
        random_int = 5
        expected_result = '5'
        self.assertEqual(say_my_name(random_int), expected_result)

if __name__ == '__main__':
    unittest.main()