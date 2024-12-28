from enigmapython.EnigmaZRotorI import EnigmaZRotorI
from enigmapython.EnigmaZRotorII import EnigmaZRotorII
from enigmapython.EnigmaZRotorIII import EnigmaZRotorIII
from enigmapython.EnigmaZEtw import EnigmaZEtw
from enigmapython.EnigmaZ import EnigmaZ
from enigmapython.ReflectorZUKW import ReflectorZUKW
import unittest


class TestEnigmaZ(unittest.TestCase):
    def test_enigma_Z_rotors_I_I_I_small_number(self):
        rotor1 = EnigmaZRotorI()
        rotor2 = EnigmaZRotorI()
        rotor3 = EnigmaZRotorI()
        reflector = ReflectorZUKW()
        etw = EnigmaZEtw()
        enigma = EnigmaZ(rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = '23041981'
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"95539350","Enigma encryption error")

    def test_enigma_Z_rotors_I_I_I_medium_number(self):
        rotor1 = EnigmaZRotorI()
        rotor2 = EnigmaZRotorI()
        rotor3 = EnigmaZRotorI()
        reflector = ReflectorZUKW()
        etw = EnigmaZEtw()
        enigma = EnigmaZ(rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = '123456789012345678901234567890'
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"719365648926063110712103315478","Enigma encryption error")

    #def test_enigma_Z_rotors_I_I_I_very_long_number(self):
    #    rotor1 = EnigmaZRotorI()
    #    rotor2 = EnigmaZRotorI()
    #    rotor3 = EnigmaZRotorI()
    #    reflector = ReflectorZUKW()
    #    etw = EnigmaZEtw()
    #    enigma = EnigmaZ(rotor3, rotor2, rotor1, reflector, etw, True)
    #    cleartext = ''
    #    my_encrypted_string = enigma.input_string(cleartext)
    #    self.assertEqual(my_encrypted_string,"","Enigma encryption error")

   
if __name__ == "__main__":
    unittest.main(verbosity=2)