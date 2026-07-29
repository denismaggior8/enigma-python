import unittest
from enigmapython.EnigmaTRotorI import EnigmaTRotorI
from enigmapython.EnigmaTRotorII import EnigmaTRotorII
from enigmapython.EnigmaTRotorIII import EnigmaTRotorIII
from enigmapython.ReflectorUKW_EnigmaT import ReflectorUKW_EnigmaT
from enigmapython.EnigmaTEtw import EnigmaTEtw
from enigmapython.EnigmaT import EnigmaT

class TestEnigmaT(unittest.TestCase):

    def test_enigma_t_basic_reciprocity(self):
        # Create components
        rotor1 = EnigmaTRotorI(position=0, ring=0)
        rotor2 = EnigmaTRotorII(position=0, ring=0)
        rotor3 = EnigmaTRotorIII(position=0, ring=0)
        reflector = ReflectorUKW_EnigmaT()
        etw = EnigmaTEtw()

        # Instantiate machine
        enigma = EnigmaT(rotor1, rotor2, rotor3, reflector, etw, auto_increment_rotors=True)

        plaintext = "tirpitzenigmajointusecode"
        ciphertext = enigma.input_string(plaintext)

        # Reset rotor positions
        rotor1.set_position(0)
        rotor2.set_position(0)
        rotor3.set_position(0)

        decrypted = enigma.input_string(ciphertext)
        self.assertEqual(decrypted, plaintext, "Decryption does not match plaintext")

    def test_enigma_t_turnover_propagation(self):
        # Enigma T Rotor I has 5 notches at E (4), K (10), Q (16), W (22), Z (25).
        # A stepping notification is triggered when the rotor steps AWAY from the notch (i.e. to notch + 1).
        # We test that stepping away from each notch increments the middle rotor.

        notches = [22, 25, 4, 10, 16]

        for notch in notches:
            rotor1 = EnigmaTRotorI(position=notch, ring=0)
            rotor2 = EnigmaTRotorII(position=0, ring=0)
            rotor3 = EnigmaTRotorIII(position=0, ring=0)
            reflector = ReflectorUKW_EnigmaT()
            etw = EnigmaTEtw()

            enigma = EnigmaT(rotor1, rotor2, rotor3, reflector, etw, auto_increment_rotors=True)

            # Stepping the first rotor once from `notch` should result in:
            # - rotor1 at (notch + 1) % 26
            # - rotor2 at 1 (since turnover propagates)
            enigma.input_char('a')

            self.assertEqual(rotor1.position, (notch + 1) % 26, f"Rotor 1 did not step correctly from notch {notch}")
            self.assertEqual(rotor2.position, 1, f"Rotor 2 did not increment when Rotor 1 stepped away from notch {notch}")

    def test_enigma_t_ring_settings(self):
        # Test with different ring settings
        rotor1 = EnigmaTRotorI(position=0, ring=10)
        rotor2 = EnigmaTRotorII(position=5, ring=5)
        rotor3 = EnigmaTRotorIII(position=10, ring=2)
        reflector = ReflectorUKW_EnigmaT()
        etw = EnigmaTEtw()

        enigma = EnigmaT(rotor1, rotor2, rotor3, reflector, etw, auto_increment_rotors=True)

        plaintext = "japanesegermancommunication"
        ciphertext = enigma.input_string(plaintext)

        # Reset positions
        rotor1.set_position(0)
        rotor2.set_position(5)
        rotor3.set_position(10)

        decrypted = enigma.input_string(ciphertext)
        self.assertEqual(decrypted, plaintext, "Decryption failed with non-zero ring settings")

    def test_enigma_t_settable_reflector(self):
        rotor1 = EnigmaTRotorI(position=0, ring=0)
        rotor2 = EnigmaTRotorII(position=0, ring=0)
        rotor3 = EnigmaTRotorIII(position=0, ring=0)
        reflector = ReflectorUKW_EnigmaT(position=3, ring=5)
        etw = EnigmaTEtw()

        enigma = EnigmaT(rotor1, rotor2, rotor3, reflector, etw)
        plaintext = "tirpitzenigma"
        ciphertext = enigma.input_string(plaintext)

        # Reset positions
        rotor1.set_position(0)
        rotor2.set_position(0)
        rotor3.set_position(0)
        reflector.set_position(3)

        decrypted = enigma.input_string(ciphertext)
        self.assertEqual(decrypted, plaintext, "Decryption failed with custom reflector position/ring")

    def test_enigma_t_long_encryption_case(self):
        # Test a long 300-character encryption using Rotors I, II, III (all at position 0, ring 0)
        # and Reflector UKW-T (position 0, ring 0)
        rotor1 = EnigmaTRotorI(position=0, ring=0)
        rotor2 = EnigmaTRotorII(position=0, ring=0)
        rotor3 = EnigmaTRotorIII(position=0, ring=0)
        reflector = ReflectorUKW_EnigmaT(position=0, ring=0)
        etw = EnigmaTEtw()

        enigma = EnigmaT(rotor1, rotor2, rotor3, reflector, etw, auto_increment_rotors=True)
        plaintext = "helloworld" * 30
        expected_ciphertext = "euoyfohmdhslsxdskfpxowoxlgxxkktjbcfrqbbkqtxhihpnvrzfpzioamnjylancxjtzviyavfzppnmndnevlzbpbcycykxfoyjftysabsgonadpfzkdwhecdiukhmcirlijpvgbknybxiuafkvrhuqnnuounhsdsukzgzukswpsxtembwfdlmfmvrmzyfxeypfsxsjpwoahdxddjeoovmauepjrrjyuskajteznbdieemjyqzvvpgluivkgwnqzxcakbzhzswqfmlwoviketomovduumyovhppvalndztq"
        
        ciphertext = enigma.input_string(plaintext)
        self.assertEqual(ciphertext, expected_ciphertext, "Encryption output does not match expected simulation value")

        # Reset positions for decryption
        rotor1.set_position(0)
        rotor2.set_position(0)
        rotor3.set_position(0)
        reflector.set_position(0)

        decrypted = enigma.input_string(ciphertext)
        self.assertEqual(decrypted, plaintext, "Decryption did not recover plaintext")

if __name__ == "__main__":
    unittest.main(verbosity=2)


