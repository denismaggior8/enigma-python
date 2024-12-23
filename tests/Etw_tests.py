from enigmapython.Etw import Etw
import unittest

class TestEtw(unittest.TestCase):

    def test_ETW_ABCDEF_process_forward(self):
        etw = Etw(wiring='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower())
        scrambled_char = etw.process_char_forward("a", 0)
        self.assertEqual(scrambled_char, 'a', "ETW forward process is wrong")

    def test_ETW_ABCDEF_process_backward(self):
        etw = Etw(wiring='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower())
        scrambled_char = etw.process_char_backward("a", -1)
        self.assertEqual(scrambled_char, 'b', "ETW backward process is wrong")

if __name__ == "__main__":
    unittest.main(verbosity=2)
