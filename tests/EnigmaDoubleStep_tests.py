import unittest
from enigmapython.EnigmaIRotorI import EnigmaIRotorI
from enigmapython.EnigmaIRotorII import EnigmaIRotorII
from enigmapython.EnigmaIRotorIII import EnigmaIRotorIII
from enigmapython.ReflectorUKWB import ReflectorUKWB
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaI import EnigmaI

class TestEnigmaDoubleStep(unittest.TestCase):
    def test_double_step_sequence(self):
        """
        Verifies the double step mechanism of the Enigma machine.
        
        Scenario:
        Rotors: I (Left), II (Middle), III (Right)
        Reflector: B
        Ring Settings: 0, 0, 0 (A, A, A)
        Start Positions: A (0), D (3), U (20)
        
        Rotor II notch is at E (4).
        Rotor III notch is at V (21).
        
        Expected Sequence:
        Start: A D U (0, 3, 20)
        1. Press key -> Right steps U->V (20->21). Right is now at notch.
           Result: A D V (0, 3, 21)
        2. Press key -> Right steps V->W (21->22). Right passing notch triggers Middle D->E (3->4).
           Result: A E W (0, 4, 22)
           Note: Middle is now at E (notch).
        3. Press key -> 
           - Right steps W->X (22->23).
           - Middle is at notch (E), so it steps E->F (4->5).
           - Middle stepping triggers Left A->B (0->1).
           Result: B F X (1, 5, 23)
        """
        # Setup
        plugboard = PlugboardPassthrough()
        etw = EtwPassthrough()
        reflector = ReflectorUKWB()
        
        # Rotors I, II, III
        # Note: EnigmaIRotorX(ring_setting, start_position)
        # We want start positions: A(0), D(3), U(20)
        # Ring settings: 0 (A)
        rotor1 = EnigmaIRotorI(0, 0)   # Left
        rotor2 = EnigmaIRotorII(3, 0)  # Middle (Start at D)
        rotor3 = EnigmaIRotorIII(20, 0) # Right (Start at U)
        
        enigma = EnigmaI(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        
        # Initial State Check
        self.assertEqual(enigma.rotors[2].position, 0, "Left rotor should be at A (0)")
        self.assertEqual(enigma.rotors[1].position, 3, "Middle rotor should be at D (3)")
        self.assertEqual(enigma.rotors[0].position, 20, "Right rotor should be at U (20)")
        
        # Step 1: Input 'A'
        enigma.input_char('a')
        # Expect: A D V (0, 3, 21)
        self.assertEqual(enigma.rotors[2].position, 0, "Step 1: Left rotor should be at A (0)")
        self.assertEqual(enigma.rotors[1].position, 3, "Step 1: Middle rotor should be at D (3)")
        self.assertEqual(enigma.rotors[0].position, 21, "Step 1: Right rotor should be at V (21)")
        
        # Step 2: Input 'A'
        enigma.input_char('a')
        # Expect: A E W (0, 4, 22)
        # Right stepped V->W, triggering Middle D->E
        self.assertEqual(enigma.rotors[2].position, 0, "Step 2: Left rotor should be at A (0)")
        self.assertEqual(enigma.rotors[1].position, 4, "Step 2: Middle rotor should be at E (4)")
        self.assertEqual(enigma.rotors[0].position, 22, "Step 2: Right rotor should be at W (22)")
        
        # Step 3: Input 'A' (The Double Step)
        enigma.input_char('a')
        # Expect: B F X (1, 5, 23)
        # Middle was at E (notch), so it steps E->F, triggering Left A->B
        # Right steps W->X
        self.assertEqual(enigma.rotors[2].position, 1, "Step 3: Left rotor should be at B (1) - Double Step Triggered")
        self.assertEqual(enigma.rotors[1].position, 5, "Step 3: Middle rotor should be at F (5) - Double Step Triggered")
        self.assertEqual(enigma.rotors[0].position, 23, "Step 3: Right rotor should be at X (23)")

if __name__ == '__main__':
    unittest.main()
