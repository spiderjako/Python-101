import unittest
from functions import sum_of_digits, to_digits, to_number, fact, fact_digits, reverse_string, palindrome, count_vowels, count_consonants, char_histogram, sum_matrix, nan_expand, char_2, prime_factorization, max_consecutive, word_counter

class TestSumOfDigits(unittest.TestCase):
    def test_if_a_number_returns_the_sum(self):
        number = 12345
        expected_result = 15
        self.assertEqual(sum_of_digits(number), expected_result)

class TestToDigits(unittest.TestCase):
    def test_if_a_number_is_turned_into_a_list_and_is_sorted(self):
        number = 12435
        expected_result = [1,2,3,4,5]
        self.assertEqual(to_digits(number), expected_result)

class TestToNumber(unittest.TestCase):
    def test_if_a_list_returns_an_integer(self):
        listy = [1,2,3,4,5]
        expected_result = 12345
        self.assertEqual(to_number(listy), expected_result)

class TestFact(unittest.TestCase):
    def test_if_an_inputed_number_returns_the_factorial(self):
        number = 5
        expected_result = 120
        self.assertEqual(fact(number), expected_result)

class TestFactDigits(unittest.TestCase):
    def test_if_a_numbers_three_digits_get_factorialised(self):
        number = 123
        expected_result = 9
        self.assertEqual(fact_digits(number), expected_result)
    def test_if_a_numbers_four_digits_get_factorialised(self):
        number = 1234
        expected_result = 33
        self.assertEqual(fact_digits(number), expected_result)

class TestReverseString(unittest.TestCase):
    def test_if_a_basic_string_gets_reversed(self):
        example = 'abcd'
        expected_result = 'dcba'
        self.assertEqual(reverse_string(example), expected_result)
    def test_if_a_string_with_numbers_gets_reversed(self):
        example = 'ab1d'
        expected_result = 'd1ba'
        self.assertEqual(reverse_string(example), expected_result)

class TestPalindrome(unittest.TestCase):
    def test_if_a_palindrome_returns_true(self):
        example = 'abcba'
        expected_result = True
        self.assertEqual(palindrome(example), expected_result)
    def test_if_a_non_palindrome_returns_false(self):
        example = 'abcd'
        expected_result = False
        self.assertEqual(palindrome(example), expected_result)

class TestCountVowels(unittest.TestCase):
    def test_if_the_vowel_count_returned_is_correct_from_the_word(self):
        example = 'word'
        expected_result = 1
        self.assertEqual(count_vowels(example), expected_result)

class TestCountCons(unittest.TestCase):
    def test_if_the_consonant_count_returned_is_correct_from_the_word(self):
        example = 'wird'
        expected_result = 3
        self.assertEqual(count_consonants(example), expected_result)

class TestCharHist(unittest.TestCase):
    def test_if_a_basic_string_returns_the_correct_value(self):
        example = 'word'
        expected_result = {'w':1,'o':1,'r':1,'d':1}
        self.assertEqual(char_histogram(example),expected_result)
    def test_if_a_more_complicated_string_returns_the_correct_value(self):
        example = 'dodo'
        expected_result = {'d':2, 'o':2}
        self.assertEqual(char_histogram(example),expected_result)

class TestSumMat(unittest.TestCase):
    def test_if_a_2x2_matrix_has_its_sum_returned(self):
        example = [[1,2],[3,4]]
        expected_result = 10
        self.assertEqual(sum_matrix(example), expected_result)
    def test_if_a_3x3_matrix_has_its_sum_returned(self):
        example = [[1,2,3],[4,5,6],[7,8,9]]
        expected_result = 45
        self.assertEqual(sum_matrix(example), expected_result)

class TestNaNExpand(unittest.TestCase):
    def test_if_the_nan_is_expanded(self):
        example = 2
        expected_result = 'Not a Not a NaN'
        self.assertEqual(nan_expand(example), expected_result)

class TestPrimeFactor(unittest.TestCase):
    def test_if_a_basic_number_is_factorised(self):
        example = 3
        expected_result = [(3,1)]
        self.assertEqual(prime_factorization(example),expected_result)
    def test_if_a_non_basic_number_gets_factorised(self):
        example = 1000
        expected_result = [(2,3),(5,3)]
        self.assertEqual(prime_factorization(example), expected_result)

class TestMaxCons(unittest.TestCase):
    def test_if_an_increasing_list_returns_the_result(self):
        example = [1,2,2,2,3,3]
        expected_result = 3
        self.assertEqual(max_consecutive(example), expected_result)
    def test_if_a_complicated_list_returns_the_result(self):
        example = [1,2,3,4,2,2,3,3,3,4,4,4,4,5,5,5,6]
        expected_result = 4
        self.assertEqual(max_consecutive(example), expected_result)
if __name__ == "__main__":
    unittest.main()