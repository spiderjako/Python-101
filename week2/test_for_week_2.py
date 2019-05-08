import unittest
from anagrams import anagrams
from week_two import gas_stations

class TestAnagrams(unittest.TestCase):
    def test_if_one_word_with_only_letters_is_an_anagram_to_another(self):
        test_subject_one = 'kilata'
        test_subject_two= 'kliata'
        expected_result = True
        self.assertEqual(anagrams(test_subject_one,test_subject_two),expected_result)
    def test_if_one_word_with_letters_and_numbers_is_an_anagram_to_another(self):
        test_subject_one = 'k1lata'
        test_subject_two = 'kl1ata'
        expected_result = True
        self.assertEqual(anagrams(test_subject_one,test_subject_two),expected_result)
    def test_if_one_word_with_different_letters_is_NOT_an_anagram_to_another(self):
        test_subject_one = 'k1lato'
        test_subject_two = 'kl1ata'
        expected_result = False
        self.assertEqual(anagrams(test_subject_one,test_subject_two),expected_result)

class TestGasStations(unittest.TestCase):
    def test_if_with_given_parameters_the_function_works(self):
        expected_result = [80,140,220,290]
        self.assertEqual(gas_stations(320,90,[50, 80, 140, 180, 220, 290]), expected_result)


if __name__ == '__main__':
    unittest.main()