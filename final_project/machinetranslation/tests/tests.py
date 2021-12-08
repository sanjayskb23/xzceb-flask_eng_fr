import unittest
import translator
class TestStringMethods(unittest.TestCase):

    def test_english_to_french_assertequal(self):
        
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        

    def test_english_to_french_assertnotequal(self):
        self.assertNotEqual(translator.english_to_french('Hello'), 'Hello')

    def test_french_to_english(self):
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
        

    def test_french_to_english_assertNotequal(self):
        self.assertNotEqual(translator.french_to_english('Bonjour'), 'Bonjour')


if __name__ == '__main__':
    unittest.main()