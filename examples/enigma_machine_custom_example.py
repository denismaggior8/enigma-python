from enigmapython.Enigma import Enigma
from enigmapython.Rotor import Rotor
from enigmapython.Reflector import Reflector
from enigmapython.SwappablePlugboard import SwappablePlugboard
from enigmapython.Etw import Etw
from enigmapython.Alphabets import Alphabets

"""
Example of creating a custom Enigma machine from scratch.
This script demonstrates how to assemble a machine using base components
(Rotor, Reflector, Enigma) instead of predefined models.
"""

def main():
    # 1. Choose an alphabet
    alphabet = Alphabets.lookup.get("latin_i18n_26chars_lowercase")
    print(f"Using alphabet: {alphabet}\n")

    # 2. Create custom rotors
    # Parameters: wiring, turnover_indexes, alphabet, initial_position, ring_setting
    # You can use historical wirings or invent your own!
    rotor1 = Rotor("ekmflgdqvzntowyhxuspaibrcj", [16], alphabet, 0, 0) # Turnover at 'q'
    rotor2 = Rotor("ajdksiruxblhwtmcqgznpyfvoe", [4], alphabet, 0, 0)  # Turnover at 'e'
    rotor3 = Rotor("bdfhjlcprtxvznyeiwgakmusqo", [21], alphabet, 0, 0) # Turnover at 'v'

    # 3. Create a custom reflector
    # In Enigma, the reflector must be reciprocal (if A->B, then B->A)
    # for encryption and decryption to be the same operation.
    reflector = Reflector("yruhqsldpxngokmiebfzcwvjat", alphabet)

    # 4. Create secondary components
    # Swappable plugboard allows you to connect pairs of letters
    plugboard = SwappablePlugboard(alphabet=alphabet)
    plugboard.swap("a", "z") # Example swap
    etw = Etw(alphabet, alphabet)

    # 5. Assemble the Enigma machine
    # The order of rotors in the list is [FastRotor, MiddleRotor, SlowRotor]
    engine = Enigma(
        plugboard=plugboard, 
        rotors=[rotor1, rotor2, rotor3], 
        reflector=reflector, 
        etw=etw, 
        auto_increment_rotors=True,
        alphabet=alphabet
    )

    # 6. Encrypt a message
    original_text = "hello"
    ciphertext = engine.input_string(original_text)
    print(f"Input:  {original_text}")
    print(f"Output: {ciphertext}")

    # 7. Decrypt (Reset rotors to original state first)
    rotor1.reset_position()
    rotor2.reset_position()
    rotor3.reset_position()
    
    decrypted_text = engine.input_string(ciphertext)
    print(f"Decrypted: {decrypted_text}")

if __name__ == "__main__":
    main()
