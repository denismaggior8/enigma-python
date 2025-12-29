import unittest
from enigmapython.EnigmaKRotorI import EnigmaKRotorI

class TestEnigmaKRotorI(unittest.TestCase):
    def test_wiring(self):
        """Test that Rotor I has the correct wiring"""
        rotor = EnigmaKRotorI(0, 0)
        self.assertEqual(rotor.wiring, 'lpgszmhaeoqkvxrfybutnicjdw')
    
    def test_notch_position(self):
        """Test that Rotor I has notch at Y (position 24)"""
        rotor = EnigmaKRotorI(0, 0)
        self.assertEqual(rotor.turnover_indexes, [24])
    
    def test_tag(self):
        """Test that Rotor I has the correct tag"""
        rotor = EnigmaKRotorI(0, 0)
        self.assertEqual(rotor.tag, "K_I")
    
    def test_position_setting(self):
        """Test that rotor position can be set correctly"""
        rotor = EnigmaKRotorI(5, 0)
        self.assertEqual(rotor.position, 5)
    
    def test_ring_setting(self):
        """Test that ring setting can be set correctly"""
        rotor = EnigmaKRotorI(0, 3)
        self.assertEqual(rotor.ring, 3)

if __name__ == '__main__':
    unittest.main()
