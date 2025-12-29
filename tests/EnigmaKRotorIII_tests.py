import unittest
from enigmapython.EnigmaKRotorIII import EnigmaKRotorIII

class TestEnigmaKRotorIII(unittest.TestCase):
    def test_wiring(self):
        """Test that Rotor III has the correct wiring"""
        rotor = EnigmaKRotorIII(0, 0)
        self.assertEqual(rotor.wiring, 'cjgdpshkturawzxfmynqobvlie')
    
    def test_notch_position(self):
        """Test that Rotor III has notch at D (position 3)"""
        rotor = EnigmaKRotorIII(0, 0)
        self.assertEqual(rotor.turnover_indexes, [13])
    
    def test_tag(self):
        """Test that Rotor III has the correct tag"""
        rotor = EnigmaKRotorIII(0, 0)
        self.assertEqual(rotor.tag, "K_III")
    
    def test_position_setting(self):
        """Test that rotor position can be set correctly"""
        rotor = EnigmaKRotorIII(5, 0)
        self.assertEqual(rotor.position, 5)
    
    def test_ring_setting(self):
        """Test that ring setting can be set correctly"""
        rotor = EnigmaKRotorIII(0, 3)
        self.assertEqual(rotor.ring, 3)

if __name__ == '__main__':
    unittest.main()
