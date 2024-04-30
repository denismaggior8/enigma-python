
from enigmapython.SwappablePlugboard import SwappablePlugboard
from string import ascii_lowercase
import unittest

class TestSwappablePlugboard(unittest.TestCase):
    
    def test_swappable_plugboard_from_a_to_z(self):
        plugboard = SwappablePlugboard()
        print(plugboard.wiring)
        plugboard.swap("a","z")
        print(plugboard.wiring)
        self.assertTrue(plugboard.wiring[0]=="z")

    def test_swappable_plugboard_from_a_to_z_reverted(self):
        plugboard = SwappablePlugboard()
        plugboard.swap("a","z")
        self.assertTrue(plugboard.wiring[25]=="a")
        

if __name__ == "__main__":
    unittest.main()