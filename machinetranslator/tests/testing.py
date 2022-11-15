#Written by trls250s for IBM Courser

import unittest

from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello, how are you today?'), "Bonjour, comment vous êtes aujourd'hui?") 
        self.assertEqual(englishToFrench("What is your name?"), "Quel est votre nom?") 
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertNotEqual(englishToFrench("The sun is nice"), "")
        

class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("Bonjour, comment vous êtes aujourd'hui?"), 'Hello, how are you today?') 
        self.assertEqual(frenchToEnglish("Quel est votre nom?"), "What is your name?")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertNotEqual(frenchToEnglish("Le soleil est"), "") 
        
unittest.main()