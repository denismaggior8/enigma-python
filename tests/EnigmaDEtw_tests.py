from enigmapython.EnigmaDEtw_QWERTZ import EnigmaDEtw_QWERTZ
from enigmapython.Alphabets import Alphabets
from enigmapython.Utils import Utils
import unittest

class TestEnigmaDEtw(unittest.TestCase):

    def test_ETW_QWERTZ_process_forward(self):
        etw = EnigmaDEtw_QWERTZ()
        # QWERTZ wiring: qwertzuioasdfghjkpyxcvbnml 
        # Calculate inverted wiring manually as Etw no longer does it
        inverted_wiring = Utils.inverse_string_permutation(etw.wiring, ''.join(etw.alphabet_list))
        
        scrambled_char = etw.scramble_char(inverted_wiring, Alphabets.lookup.get('latin_i18n_26chars_lowercase').index("a"), 0)
        self.assertEqual(scrambled_char, 'j', "ETW forward process is wrong")

    def test_ETW_QWERTZ_process_backward(self):
        etw = EnigmaDEtw_QWERTZ()
        inverted_wiring = Utils.inverse_string_permutation(etw.wiring, ''.join(etw.alphabet_list))
        
        # Backward process: Input 'j' should return 'a' (inverse of Forward A->J)
        # We must simulate backward passage: Find index in inverted_wiring, map to alphabet.
        # But wait, ScrambleChar method in Enigma.py return path calls:
        # scramble_char(alphabet, wiring.index(char), ...)
        
        input_char =    'q'
        # Emulate backward pass manually using Enigma's return path logic logic
        # For ETW return: index in wiring -> char in alphabet
        # Note: Enigma return path uses self.etw.wiring (RAW) as of my last revert?
        # WAIT. I reverted Enigma.py return path to use INVERTED_WIRING in Step 117?
        # YES. "Reverting Enigma.py return path to use inverted_wiring as requested"
        # So I should use inverted_wiring.index(char).
        
        scrambled_char = etw.scramble_char(etw.alphabet_list, inverted_wiring.index(input_char), 0)
        
        self.assertEqual(scrambled_char, 'k', "ETW backward process is wrong")
    
    def test_ETW_QWERTZ_wiring(self):
        etw = EnigmaDEtw_QWERTZ()
        # etw.wiring should now be the raw QWERTZ string since Etw class doesn't invert it 
        self.assertEqual(etw.wiring, 'qwertzuioasdfghjkpyxcvbnml', "QWERTZ ETW wiring is wrong")

if __name__ == "__main__":
    unittest.main(verbosity=2)