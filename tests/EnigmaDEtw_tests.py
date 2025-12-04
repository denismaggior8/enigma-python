from enigmapython.EnigmaDEtw_JWULCM import EnigmaDEtw_JWULCM
from enigmapython.EnigmaDEtw_QWERTZ import EnigmaDEtw_QWERTZ
from enigmapython.Alphabets import Alphabets
import unittest

class TestEnigmaDEtw(unittest.TestCase):

    def test_ETW_JWULCM_process_forward(self):
        etw = EnigmaDEtw_JWULCM()
        scrambled_char = etw.scramble_char(etw.wiring, Alphabets.lookup.get('latin_i18n_26chars_lowercase').index("a"), 0)
        self.assertEqual(scrambled_char, 'j', "ETW forward process is wrong")

    def test_ETW_JWULCM_process_backward(self):
        etw = EnigmaDEtw_JWULCM()
        scrambled_char = etw.scramble_char(etw.wiring, Alphabets.lookup.get('latin_i18n_26chars_lowercase').index("b"), 1)
        self.assertEqual(scrambled_char, 'u', "ETW backward process is wrong")
    
    def test_ETW_QWERTZ_wiring(self):
        etw = EnigmaDEtw_QWERTZ()
        self.assertEqual(etw.wiring, 'qwertzuioasdfghjkpyxcvbnml', "QWERTZ ETW wiring is wrong")

if __name__ == "__main__":
    unittest.main(verbosity=2)