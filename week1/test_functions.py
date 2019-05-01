import unittest
from functions import sum_of_digits, to_digits, to_number, fact

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

if __name__ == "__main__":
    unittest.main()