
import unittest
from enigmapython.EnigmaIRotorI import EnigmaIRotorI

class TestSettableRotor(unittest.TestCase):
    
    def test_initial_state(self):
        """Test initial state of a Rotor"""
        rotor = EnigmaIRotorI(position=0, ring=0)
        self.assertEqual(rotor.position, 0)
        self.assertEqual(rotor.ring, 0)
        self.assertEqual(rotor.wiring, "ekmflgdqvzntowyhxuspaibrcj")
        self.assertEqual(rotor.dot_position, 20)

    def test_set_position(self):
        """Test setting the position"""
        rotor = EnigmaIRotorI(position=0, ring=0)
        rotor.set_position(5)
        self.assertEqual(rotor.position, 5)
        self.assertEqual(rotor.ring, 0)
        self.assertEqual(rotor.wiring, "ekmflgdqvzntowyhxuspaibrcj") # Wiring doesn't change with position

    def test_set_ring(self):
        """Test setting the ring setting"""
        rotor = EnigmaIRotorI(position=0, ring=0)
        rotor.set_ring(1) # Ring setting B
        self.assertEqual(rotor.position, 0)
        self.assertEqual(rotor.ring, 1)
        self.assertEqual(rotor.wiring, "kflngmherwaoupxziyvtqbjcsd")
        self.assertEqual(rotor.dot_position, 21)

    def test_reset_position(self):
        """Test resetting the position"""
        rotor = EnigmaIRotorI(position=10, ring=5)
        rotor.reset_position()
        self.assertEqual(rotor.position, 0)
        self.assertEqual(rotor.ring, 5) # Ring should verify
        
    def test_reset_ring(self):
        """Test resetting the ring setting"""
        rotor = EnigmaIRotorI(position=10, ring=5)
        rotor.reset_ring()
        self.assertEqual(rotor.position, 10) # Position should verify
        self.assertEqual(rotor.ring, 0)
        self.assertEqual(rotor.wiring, "ekmflgdqvzntowyhxuspaibrcj")
        
    def test_interleaved_operations(self):
        """Test a sequence of operations"""
        rotor = EnigmaIRotorI(position=0, ring=0)
        
        # 1. Set Ring to 5
        rotor.set_ring(5)
        self.assertEqual(rotor.ring, 5)
        initial_wiring_5 = rotor.wiring
        
        # 2. Set Position to 10
        rotor.set_position(10)
        self.assertEqual(rotor.position, 10)
        
        # 3. Reset Ring (should go to 0, wiring reset)
        rotor.reset_ring()
        self.assertEqual(rotor.ring, 0)
        self.assertEqual(rotor.wiring, "ekmflgdqvzntowyhxuspaibrcj")
        self.assertEqual(rotor.position, 10) # Position maintained
        
        # 4. Set Ring back to 5
        rotor.set_ring(5)
        self.assertEqual(rotor.wiring, initial_wiring_5)
        
        # 5. Reset Position
        rotor.reset_position()
        self.assertEqual(rotor.position, 0)
        self.assertEqual(rotor.ring, 5)

    def test_reset_position_resets_counter(self):
        """Test that reset_position also resets the rotations_counter in Rotor"""
        rotor = EnigmaIRotorI(position=0, ring=0)
        rotor.increment_position()
        rotor.increment_position()
        self.assertEqual(rotor.rotations_counter, 2)
        
        rotor.reset_position()
        self.assertEqual(rotor.position, 0)
        self.assertEqual(rotor.rotations_counter, 0, "reset_position should reset rotations_counter via set_position")

if __name__ == '__main__':
    unittest.main()
