import unittest, translator

class TestMethods(unittest.TestCase):
    def test_french_null(self):
        self.assertIsNotNone(translator.french_to_english(' '), 'It is null')
    def test_english_null(self):
        self.assertIsNotNone(translator.english_to_french(' '), 'It is null')
    def test_french_trans(self):
        self.assertEqual(translator.french_to_english('Bonjour'),'Hello')
    def test_english_trans(self):
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')


if __name__ == "__main__":
    unittest.main()