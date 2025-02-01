from enigmapython.Etw import Etw
from enigmapython.Alphabets import Alphabets    
import unittest

class TestEtw(unittest.TestCase):

    def test_ETW_ABCDEF_process_forward(self):
        etw = Etw(wiring='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower())
        scrambled_char = etw.scramble_char(etw.wiring,Alphabets.lookup.get('latin_i18n_26chars_lowercase').index("a"),0)
        self.assertEqual(scrambled_char, 'a', "ETW forward process is wrong")

    def test_ETW_ABCDEF_process_backward(self):
        etw = Etw(wiring='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower())
        scrambled_char = etw.scramble_char(etw.wiring,Alphabets.lookup.get('latin_i18n_26chars_lowercase').index("a"),1)
        self.assertEqual(scrambled_char, 'b', "ETW backward process is wrong")

    def test_ETW_ABCDEF_process_backward_negative_shift(self):
        etw = Etw(wiring='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower())
        scrambled_char = etw.scramble_char(etw.wiring,Alphabets.lookup.get('latin_i18n_26chars_lowercase').index("a"),-1)
        self.assertEqual(scrambled_char, 'z', "ETW backward process is wrong")

if __name__ == "__main__":
    unittest.main(verbosity=2)
