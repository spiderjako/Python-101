import unittest
from rpn_calculate import rpn_calculate


class TestReversedPolishNotation(unittest.TestCase):
    def test_if_two_numbers_are_conjoined_through_operator(self):
        expression = '5 6 +'
        expected_result = 11

        self.assertEqual(rpn_calculate(expression), expected_result)
    def test_if_the_expression_with_multiple_operators(self):
        expression = '4 2 + 3 -'
        expected_result = 3

        self.assertEqual(rpn_calculate(expression), expected_result)

if __name__ == '__main__':
    unittest.main()