import unittest

from translator import english_to_french, french_to_english

class TestE2f(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(''), '') # test when null is given as input the output is null.
        self.assertEqual(english_to_french('Hello'),'Bonjour')  # test when 'Hello' is given as input the output is 'Bonjour'.


class TestF2e(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(''), '') # test when null is given as input the output is null.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'

# Andrii Novyk's test.py file.