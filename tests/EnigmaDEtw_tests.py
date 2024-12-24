from enigmapython.Etw import Etw
import unittest

class TestEnigmaDEtw(unittest.TestCase):

    def test_ETW_JWULCM_process_forward(self):
        etw = Etw(wiring='JWULCMNOHPQZYXIRADKEGVBTSF'.lower())
        scrambled_char = etw.process_char_forward("a", 0)
        self.assertEqual(scrambled_char, 'j', "ETW forward process is wrong")

    def test_ETW_JWULCM_process_backward(self):
        etw = Etw(wiring='JWULCMNOHPQZYXIRADKEGVBTSF'.lower())
        scrambled_char = etw.process_char_backward("b", 1)
        self.assertEqual(scrambled_char, 'q', "ETW backward process is wrong")

if __name__ == "__main__":
    unittest.main(verbosity=2)