from enigmapython.EtwQWERTZ import EtwQWERTZ
from enigmapython.Alphabets import Alphabets
from enigmapython.Utils import Utils
import unittest

class TestEtwQWERTZ(unittest.TestCase):

    def test_ETW_QWERTZ_process_forward(self):
        etw = EtwQWERTZ()
        # QWERTZ wiring: qwertzuioasdfghjkpyxcvbnml 
        # Calculate inverted wiring manually as Etw no longer does it
        inverted_wiring = Utils.inverse_string_permutation(etw.wiring, ''.join(etw.alphabet_list))
        
        scrambled_char = etw.scramble_char(inverted_wiring, Alphabets.lookup.get('latin_i18n_26chars_lowercase').index("a"), 0)
        self.assertEqual(scrambled_char, 'j', "ETW forward process is wrong")

    def test_ETW_QWERTZ_process_backward(self):
        etw = EtwQWERTZ()
        inverted_wiring = Utils.inverse_string_permutation(etw.wiring, ''.join(etw.alphabet_list))
        
        # Backward process logic matching original test
        input_char = 'q'     
        scrambled_char = etw.scramble_char(etw.alphabet_list, inverted_wiring.index(input_char), 0)
        
        self.assertEqual(scrambled_char, 'k', "ETW backward process is wrong")
    
    def test_ETW_QWERTZ_wiring(self):
        etw = EtwQWERTZ()
        self.assertEqual(etw.wiring, 'qwertzuioasdfghjkpyxcvbnml', "QWERTZ ETW wiring is wrong")

if __name__ == "__main__":
    unittest.main(verbosity=2)
