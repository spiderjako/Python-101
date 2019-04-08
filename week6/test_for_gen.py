import unittest

from generators import chain, compress

class TestChain(unittest.TestCase):
    def test_if_iterables_are_passed_to_chain_list_of_both_is_returned(self):
        expected_result = [0,1,2,3,4,5,6,7]
        actual_result = list(chain(range(0,4), range(4,8)))
        self.assertEqual(expected_result, actual_result)
    def test_if_when_sets_are_passed_list_of_both_is_returned(self):
        expected_result = [1,2,3,3,4,5]
        actual_result = list(chain({1,2,3}, {3,4,5}))
        self.assertEqual(expected_result, actual_result)
    def test_if_when_list_and_set_are_passed_list_of_both_is_returned(self):
        expected_result = [1,2,3,3,4,5,6]
        actual_result = list(chain([1,2,3],{3,4,5,6}))
        self.assertEqual(expected_result, actual_result)

class TestCompress(unittest.TestCase):
    def test_if_two_lists_return_the_expected_values(self):
        actual_result = list(compress(['Panda','Lion', 'BMW'], [False,False,True]))
        expected_result = ['BMW']
        self.assertEqual(actual_result, expected_result)
    def test_if_list_and_set_return_expected_result(self):
        actual_result = list(compress(['BMW','Ford','Mini'], [True, False, False]))
        expected_result = ['BMW']
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()