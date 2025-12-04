import unittest
from enigmapython.EnigmaKEtw_QWERTZ import EnigmaKEtw_QWERTZ

class TestEnigmaKEtw_QWERTZ(unittest.TestCase):
    def test_wiring(self):
        """Test that ETW has the correct QWERTZ wiring"""
        etw = EnigmaKEtw_QWERTZ()
        self.assertEqual(etw.wiring, 'qwertzuioasdfghjkpyxcvbnml')
    
    def test_qwertz_layout(self):
        """Test that ETW follows QWERTZ keyboard layout"""
        etw = EnigmaKEtw_QWERTZ()
        # First 6 letters should be QWERTZ
        self.assertEqual(etw.wiring[:6], 'qwertz')
    
    def test_inheritance(self):
        """Test that EnigmaKEtw_QWERTZ inherits from EtwQWERTZ"""
        etw = EnigmaKEtw_QWERTZ()
        self.assertEqual(etw.__class__.__bases__[0].__name__, 'EtwQWERTZ')

if __name__ == '__main__':
    unittest.main()
