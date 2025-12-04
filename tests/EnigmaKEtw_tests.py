import unittest
from enigmapython.EnigmaKEtw import EnigmaKEtw

class TestEnigmaKEtw(unittest.TestCase):
    def test_wiring(self):
        """Test that ETW has the correct QWERTZ wiring"""
        etw = EnigmaKEtw()
        self.assertEqual(etw.wiring, 'qwertzuioasdfghjkpyxcvbnml')
    
    def test_qwertz_layout(self):
        """Test that ETW follows QWERTZ keyboard layout"""
        etw = EnigmaKEtw()
        # First 6 letters should be QWERTZ
        self.assertEqual(etw.wiring[:6], 'qwertz')

if __name__ == '__main__':
    unittest.main()
