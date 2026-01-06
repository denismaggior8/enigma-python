import unittest
from enigmapython.Enigma import Enigma
from enigmapython.Rotor import Rotor
from enigmapython.Reflector import Reflector
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.Etw import Etw
from enigmapython.Alphabets import Alphabets

class TestCustomEnigma(unittest.TestCase):
    def test_custom_enigma_configuration(self):
        # 1. Define alphabet
        alphabet = Alphabets.lookup.get("latin_i18n_26chars_lowercase")

        # 2. Create custom rotors
        # Parameters: wiring, turnover_indexes, alphabet, initial_position, ring_setting
        # These match Enigma I rotors I, II, III for a predictable result
        rotor1 = Rotor("ekmflgdqvzntowyhxuspaibrcj", [16], alphabet, 0, 0) # Turnover at 'q'
        rotor2 = Rotor("ajdksiruxblhwtmcqgznpyfvoe", [4], alphabet, 0, 0)  # Turnover at 'e'
        rotor3 = Rotor("bdfhjlcprtxvznyeiwgakmusqo", [21], alphabet, 0, 0) # Turnover at 'v'

        # 3. Create custom reflector
        reflector = Reflector("yruhqsldpxngokmiebfzcwvjat", alphabet)

        # 4. Create components
        plugboard = PlugboardPassthrough(alphabet)
        etw = Etw(alphabet, alphabet)

        # 5. Assemble the Enigma machine
        engine = Enigma(plugboard, [rotor1, rotor2, rotor3], reflector, etw, auto_increment_rotors=True, alphabet=alphabet)

        # 6. Encrypt/Decrypt
        input_text = "hello"
        ciphertext = engine.input_string(input_text)
        
        # Verify it produces a result (with these settings 'hello' -> 'mfncz')
        self.assertEqual(ciphertext, "mfncz")
        
        # 7. Decrypt - Reset machine to original state
        rotor1.reset_position()
        rotor2.reset_position()
        rotor3.reset_position()
        
        decrypted = engine.input_string(ciphertext)
        self.assertEqual(decrypted, input_text)

if __name__ == "__main__":
    unittest.main()
