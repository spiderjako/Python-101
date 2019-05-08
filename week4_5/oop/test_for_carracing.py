import unittest
from carracing import Car,Driver

class TestCar(unittest.TestCase):
    def test_if_car_gets_printed_out_with_dunder(self):
        test_subject = Car('a','b',300)
        expected_result = 'a b with 300 maximum speed.'
        self.assertEqual(str(test_subject),expected_result)
    def test_if_driver_gets_printed_out_with_dunder(self):
        test_car = Car('c','d',300)
        test_subject = Driver('a',test_car)
        expected_result = 'a has a c d with 300 maximum speed.'
        self.assertEqual(str(test_subject),expected_result)
if __name__=='__main__':
    unittest.main()