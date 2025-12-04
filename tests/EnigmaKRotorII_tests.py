import unittest
from enigmapython.EnigmaKRotorII import EnigmaKRotorII

class TestEnigmaKRotorII(unittest.TestCase):
    def test_wiring(self):
        """Test that Rotor II has the correct wiring"""
        rotor = EnigmaKRotorII(0, 0)
        self.assertEqual(rotor.wiring, 'slvgbtfxjqohewirzyamkpcndu')
    
    def test_notch_position(self):
        """Test that Rotor II has notch at M (position 12)"""
        rotor = EnigmaKRotorII(0, 0)
        self.assertEqual(rotor.notch_indexes, [12])
    
    def test_tag(self):
        """Test that Rotor II has the correct tag"""
        rotor = EnigmaKRotorII(0, 0)
        self.assertEqual(rotor.tag, "K_II")
    
    def test_position_setting(self):
        """Test that rotor position can be set correctly"""
        rotor = EnigmaKRotorII(5, 0)
        self.assertEqual(rotor.position, 5)
    
    def test_ring_setting(self):
        """Test that ring setting can be set correctly"""
        rotor = EnigmaKRotorII(0, 3)
        self.assertEqual(rotor.ring, 3)

if __name__ == '__main__':
    unittest.main()
