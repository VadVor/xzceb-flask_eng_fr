import unittest
#from translator import englishToFrench, frenchToEnglish
from machinetranslation import translator

class TestEngToFr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.englishToFrench('Null'), 'Null') 
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')  
        
class TestFrToEng(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.frenchToEnglish('Null'), 'Null') 
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello') 
        
unittest.main()