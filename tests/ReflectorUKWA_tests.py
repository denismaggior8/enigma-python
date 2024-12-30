
from enigmapython.ReflectorUKWA import ReflectorUKWA
from string import ascii_lowercase
import unittest

class TestReflectorUKWA(unittest.TestCase):

    # Test according to Cryptomuseum at https://www.cryptomuseum.com/crypto/enigma/wiring.htm#10
    def test_reflector_a_wiring(self):
        reflector = ReflectorUKWA()
        self.assertEqual(reflector.wiring,"EJMZALYXVBWFCRQUONTSPIKHGD".lower(),"Wiring error")
    
    def test_reflector_a_scramble_char_z(self):
        reflector = ReflectorUKWA()
        char = "z"
        scrambled_char = reflector.scramble_char(reflector.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"d","Scramble error")

    def test_reflector_a_scramble_char_e(self):
        reflector = ReflectorUKWA()
        char = "e"
        scrambled_char = reflector.scramble_char(reflector.wiring,list(ascii_lowercase).index(char),0)
        self.assertEqual(scrambled_char,"a","Scramble error")

if __name__ == "__main__":
    unittest.main()