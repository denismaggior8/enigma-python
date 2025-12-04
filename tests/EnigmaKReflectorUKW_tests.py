import unittest
from enigmapython.EnigmaKReflectorUKW import EnigmaKReflectorUKW

class TestEnigmaKReflectorUKW(unittest.TestCase):
    def test_wiring(self):
        """Test that Reflector UKW has the correct wiring"""
        reflector = EnigmaKReflectorUKW()
        self.assertEqual(reflector.wiring, 'imetcgfraysqbzxwlhkdvupojn')
    
    def test_tag(self):
        """Test that Reflector UKW has the correct tag"""
        reflector = EnigmaKReflectorUKW()
        self.assertEqual(reflector.tag, "K_UKW")
    
    def test_reciprocal_wiring(self):
        """Test that reflector wiring is reciprocal (if A->I, then I->A)"""
        reflector = EnigmaKReflectorUKW()
        wiring = reflector.wiring
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        for i, char in enumerate(alphabet):
            mapped_char = wiring[i]
            mapped_index = alphabet.index(mapped_char)
            reverse_mapped = wiring[mapped_index]
            self.assertEqual(reverse_mapped, char, 
                           f"Reflector wiring not reciprocal: {char}->{mapped_char} but {mapped_char}->{reverse_mapped}")

if __name__ == '__main__':
    unittest.main()
