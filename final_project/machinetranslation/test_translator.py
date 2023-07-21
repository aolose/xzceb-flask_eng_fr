"""Test for translator"""
import unittest
import translator

HELLO_EN = 'Hello'
HELLO_FR = 'Bonjour'
GOOD_EVENING_EN = 'Good evening'
GOOD_EVENING_FR = 'Bonne soirée'


class TestTranslator(unittest.TestCase):
    """5.Write unit tests to test the above functions. (4)"""

    def test_french_equal_english(self):
        """a. assertEqual frenchToEnglish"""
        self.assertEqual(translator.frenchToEnglish(HELLO_FR),
                         HELLO_EN, 'should equal')

    def test_french_not_equal_english(self):
        """b. assertNotEqual frenchToEnglish"""
        self.assertNotEqual(translator.frenchToEnglish(HELLO_FR),
                            GOOD_EVENING_EN, 'should not equal')

    def test_english_equal_french(self):
        """c. assertEqual englishToFrench"""
        self.assertEqual(translator.englishToFrench(HELLO_EN),
                         HELLO_FR, 'should equal')

    def test_english_no_equal_french(self):
        """d. assertNotEqual englishToFrench"""
        self.assertNotEqual(translator.englishToFrench(HELLO_EN),
                            GOOD_EVENING_FR, 'should not equal')


if __name__ == '__main__':
    unittest.main()
