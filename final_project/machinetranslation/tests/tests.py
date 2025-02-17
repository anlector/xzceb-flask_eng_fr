import unittest
from translator import english_to_french, french_to_english

class TestE2f(unittest.TestCase): 
    def test1(self): 
        
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Hello'),'Hello') 

class TestF2e(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
        
unittest.main()
# Andrii Novyk's test.py file.