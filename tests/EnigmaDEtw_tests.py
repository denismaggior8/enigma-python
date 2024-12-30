from enigmapython.Etw import Etw
from enigmapython.Enigma import Enigma  
from enigmapython.Alphabets import Alphabets
import unittest

class TestEnigmaDEtw(unittest.TestCase):

    def test_ETW_JWULCM_process_forward(self):
        etw = Etw(wiring='JWULCMNOHPQZYXIRADKEGVBTSF'.lower())
        scrambled_char = etw.scramble_char(etw.wiring,Alphabets.lookup.get('latin_i18n_26chars_lowercase').index("a"),0)
        self.assertEqual(scrambled_char, 'j', "ETW forward process is wrong")

    def test_ETW_JWULCM_process_backward(self):
        etw = Etw(wiring='JWULCMNOHPQZYXIRADKEGVBTSF'.lower())
        scrambled_char = etw.scramble_char(etw.wiring,Alphabets.lookup.get('latin_i18n_26chars_lowercase').index("b"),1)
        self.assertEqual(scrambled_char, 'u', "ETW backward process is wrong")

if __name__ == "__main__":
    unittest.main(verbosity=2)