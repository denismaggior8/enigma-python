import unittest
from enigmapython.EnigmaM4RotorVIII import EnigmaM4RotorVIII
from enigmapython.EnigmaM4RotorIII import EnigmaM4RotorIII
from enigmapython.EnigmaM4RotorIV import EnigmaM4RotorIV
from enigmapython.EnigmaM4RotorGamma import EnigmaM4RotorGamma
from enigmapython.ReflectorUKWBThin import ReflectorUKWBThin
from enigmapython.SwappablePlugboard import SwappablePlugboard
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaM4 import EnigmaM4

class TestEnigmaM4U534(unittest.TestCase):
    def test_u534_p1030700_decryption(self):
        """
        Verifies the decryption of the U534 M4 message P1030700.
        Source: https://enigma.hoerenberg.com/index.php?cat=The%20U534%20messages&page=P1030700
        
        Settings:
        Enigma Model: M4
        Reflector: B Thin
        Greek Rotor: Gamma (C)
        Rotors: IV, III, VIII (Left to Right) -> VIII Right, III Middle, IV Left
        Ring Settings: AACU -> Gamma: A(0), IV: A(0), III: C(2), VIII: U(20)
        Plugboard: CH EJ NV OU TY LG SZ PK DI QB
        Grundstellung: VMGC -> Gamma: V, IV: M, III: G, VIII: C
        
        Message Indicator: ROGU MMDG
        """
        # Setup Plugboard
        plugboard = SwappablePlugboard()
        plugboard.swap("c", "h")
        plugboard.swap("e", "j")
        plugboard.swap("n", "v")
        plugboard.swap("o", "u")
        plugboard.swap("t", "y")
        plugboard.swap("l", "g")
        plugboard.swap("s", "z")
        plugboard.swap("p", "k")
        plugboard.swap("d", "i")
        plugboard.swap("q", "b")
        
        # Setup Rotors
        # EnigmaM4(plugboard, rotor1(Right), rotor2(Middle), rotor3(Left), rotor4(Greek), ...)
        
        # Right Rotor (VIII): Ring U (20), Pos C (2)
        # Note: Constructor is (position, ring)
        # Grundstellung C -> 2
        rotor_right = EnigmaM4RotorVIII(2, 20)
        
        # Middle Rotor (III): Ring C (2), Pos G (6)
        rotor_middle = EnigmaM4RotorIII(6, 2)
        
        # Left Rotor (IV): Ring A (0), Pos M (12)
        rotor_left = EnigmaM4RotorIV(12, 0)
        
        # Greek Rotor (Gamma): Ring A (0), Pos V (21)
        rotor_greek = EnigmaM4RotorGamma(21, 0)
        
        reflector = ReflectorUKWBThin()
        etw = EtwPassthrough()
        
        enigma = EnigmaM4(plugboard, rotor_right, rotor_middle, rotor_left, rotor_greek, reflector, etw, True)
        
        # 1. Set Message Key directly (VMGC)
        # The site lists "Wheel positions: VMGC", which appears to be the final message key.
        # Greek: V (21), Left: M (12), Middle: G (6), Right: C (2)
        
        enigma.rotors[3].position = 21 # V
        enigma.rotors[2].position = 12 # M
        enigma.rotors[1].position = 6  # G
        enigma.rotors[0].position = 2  # C
             
        # 2. Decrypt Ciphertext
        ciphertext_block1 = "QBHEWTDFEQITKUWFQUHLIQQGVYGRSDOHDCOBFMDHXSKOFPAODRSVBEREIQZVEDAXSHOHBIYMCIIZSKGNDLNFKFVLWWHZXZGQXWSSPWLSOQXEANCELJYJCETZTLSTTWMTOBW".lower()
        expected_plaintext_block1 = "KOMXBDMXUUUBOOTEYFXDXUUUAUSBILVUNYYZWOSECHSXUUUFLOTTXVVVUUURWODREISECHSVIERKKREMASKKMITUUVZWODREIFUVFYEWHSYUUUZWODREIFUNFZWOYUUFZWL".lower()
        
        plaintext = enigma.input_string(ciphertext_block1)
        
        print(f"Decrypted Plaintext: {plaintext}")
        
        self.assertEqual(plaintext, expected_plaintext_block1, "M4 U534 decryption failed")

if __name__ == '__main__':
    unittest.main()
