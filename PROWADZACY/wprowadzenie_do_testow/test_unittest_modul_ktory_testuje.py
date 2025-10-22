import unittest
from modul_ktory_testuje import funkcja

class TestTestowanaFunkcja(unittest.TestCase):

    def test_funkcja_dla_wartosci_ujemnych(self):
        result = funkcja(-1)
        expected = 0
        self.assertEqual(result, expected)


    def test_funkcja_dla_wartosci_0(self):
        result = funkcja(0)
        expected = 0
        self.assertEqual(result, expected)

    def test_funkcja_dla_wartosci_dodatniej(self):
        result = funkcja(1)
        expected = 1
        self.assertEqual(result, expected)