import unittest

from funky import simplify_fraction, collect_fractions, sort_fractions

class TestSimplifyFraction(unittest.TestCase):
    def test_if_two_prime_numbers_division_return_prime_numbers(self):
        nominator = 2
        denominator = 5
        expected_result = (2,5)
        self.assertEqual(simplify_fraction((nominator,denominator)),expected_result)

    def test_if_two_non_prime_numbers_with_modulo_denominator_which_is_not_zero_returns_the_right_fraction(self):
        nominator = 4
        denominator = 10
        expected_result = (2,5)
        self.assertEqual(simplify_fraction((nominator,denominator)), expected_result)

    def test_if_two_non_prime_numbers_with_modulo_denominator_which_is_zero_returns_the_right_fraction(self):
        nominator = 3
        denominator = 9
        expected_result = (1,3)
        self.assertEqual(simplify_fraction((nominator,denominator)), expected_result)

    def test_if_two_equal_numbers_division_return_one(self):
        nominator = 3
        denominator = 3
        expected_result = (1,1)
        self.assertEqual(simplify_fraction((nominator,denominator)), expected_result)
    def test_validate_fraction_object_is_a_tuple(self):
        with self.assertRaises(Exception) as exc:
            simplify_fraction((1,2))
        self.assertError('', exc.exception)

class TestCollectFractions(unittest.TestCase):
    def test_if_two_touples_give_the_result(self):
        first_touple = (1,2)
        second_touple = (1,4)
        expected_result = (3,4)
        self.assertEqual(collect_fractions([first_touple, second_touple]), expected_result)
    def test_if_more_than_two_touples_give_the_result(self):
        first_touple = (1,2)
        second_touple = (2,3)
        third_touple = (3,4)
        expected_result = (23,12)
        self.assertEqual(collect_fractions([first_touple, second_touple, third_touple]), expected_result)

class TestSortFractions(unittest.TestCase):
    def test_if_two_tuples_are_sorted_out(self):
        list_tuples = [(2,3),(1,2)]
        expected_result = [(1,2), (2,3)]
        self.assertEqual(sort_fractions(list_tuples), expected_result)
    def test_if_more_than_two_tuples_are_sorted_out(self):
        list_tuples = [(2,3),(1,2),(7,6), (5,6)]
        expected_result = [(1,2), (2,3), (5,6), (7,6)]
        self.assertEqual(sort_fractions(list_tuples), expected_result)


if __name__ == '__main__':
    unittest.main()