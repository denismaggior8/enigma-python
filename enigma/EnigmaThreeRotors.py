from Enigma import Enigma
from enigma.RotorWiringI import RotorWiringI
from enigma.RotorWiringII import RotorWiringII
from enigma.RotorWiringIII import RotorWiringIII
from enigma.PlugboardPassthrough import PlugboardPassthrough
from enigma.ReflectorUKWB import ReflectorUKWB
from enigma.EtwPassthrough import EtwPassthrough
import unittest

class EnigmaThreeRotors(Enigma):
   
    def __init__(self,plugboard,rotor1, rotor2, rotor3,reflector,etw):
         rotors = [rotor1, rotor2, rotor3]
         super().__init__(plugboard,rotors,reflector,etw)

class TestEnigma(unittest.TestCase):
     
    def test_enigma_output(self):
        plugboard = PlugboardPassthrough()
        rotor1 = RotorWiringI(25)
        rotor2 = RotorWiringII(25)
        rotor3 = RotorWiringIII(25)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaThreeRotors(plugboard,rotor1,rotor2,rotor3,reflector,etw)
        self.assertEqual(enigma.input_char("z"),"t","Enigma output error")

    def test_enigma_output_reverted(self):
        plugboard = PlugboardPassthrough()
        rotor1 = RotorWiringI(25)
        rotor2 = RotorWiringII(25)
        rotor3 = RotorWiringIII(25)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaThreeRotors(plugboard,rotor1,rotor2,rotor3,reflector,etw)
        scrambled_char = enigma.input_char("z")
        self.assertEqual(enigma.input_char(scrambled_char),"z","Enigma output error")

if __name__ == "__main__":
    unittest.main()