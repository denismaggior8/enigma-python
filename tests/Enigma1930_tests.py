import unittest
from enigmapython.EnigmaIRotorI import EnigmaIRotorI
from enigmapython.EnigmaIRotorII import EnigmaIRotorII
from enigmapython.EnigmaIRotorIII import EnigmaIRotorIII
from enigmapython.ReflectorUKWA import ReflectorUKWA
from enigmapython.SwappablePlugboard import SwappablePlugboard
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaI import EnigmaI

class TestEnigma1930(unittest.TestCase):
    def test_1930_message_decryption(self):
        """
        Verifies the decryption of the authentic 1930 German Army Enigma test message.
        Source: https://cryptocellar.org/enigma/e-message-1930.html

        Settings:
        Enigma Model: I
        Reflector: A
        Rotors: II I III (Left to Right) -> III is Right (Fast), II is Left (Slow)
        Ring Settings: 24 13 22 (X M V) -> 23 12 21 (0-based)
        Grundstellung: 06 15 12 (F O L) -> 05 14 11 (0-based)
        Stecker: A/M, F/I, N/V, P/S, T/U, W/Z
        """
        # Setup Plugboard
        plugboard = SwappablePlugboard()
        plugboard.swap("a", "m")
        plugboard.swap("f", "i")
        plugboard.swap("n", "v")
        plugboard.swap("p", "s")
        plugboard.swap("t", "u")
        plugboard.swap("w", "z")
        
        # Setup Rotors
        # Note: EnigmaIRotorX(position, ring)
        # Right Rotor (III): Pos 12 (L) -> 11, Ring 22 (V) -> 21
        rotor_right = EnigmaIRotorIII(11, 21)
        
        # Middle Rotor (I): Pos 15 (O) -> 14, Ring 13 (M) -> 12
        rotor_middle = EnigmaIRotorI(14, 12)
        
        # Left Rotor (II): Pos 06 (F) -> 5, Ring 24 (X) -> 23
        rotor_left = EnigmaIRotorII(5, 23)
        
        reflector = ReflectorUKWA()
        etw = EtwPassthrough()
        
        # EnigmaI(plugboard, right, middle, left, reflector, etw, auto_increment)
        enigma = EnigmaI(plugboard, rotor_right, rotor_middle, rotor_left, reflector, etw, True)
        
        # 1. Decrypt Message Key
        # Encrypted Message Key: PKPJXI
        encrypted_key = "PKPJXI".lower()
        decrypted_key = enigma.input_string(encrypted_key)
        
        self.assertEqual(decrypted_key, "ablabl", "Message key decryption failed")
        
        # 2. Reconfigure Rotors to Message Key (ABL)
        # A -> 0, B -> 1, L -> 11
        # Order is Left, Middle, Right? Or Right, Middle, Left?
        # Usually message key is given Left to Right (Slow to Fast).
        # So Left=A(0), Middle=B(1), Right=L(11).
        
        # Update positions
        # Note: We need to access the rotors in the enigma instance to ensure we are modifying the active ones
        # enigma.rotors[0] is Right, [1] is Middle, [2] is Left
        
        enigma.rotors[2].position = 0   # Left (A)
        enigma.rotors[1].position = 1   # Middle (B)
        enigma.rotors[0].position = 11  # Right (L)
        
        # 3. Decrypt Ciphertext
        ciphertext = "GCDSE AHUGW TQGRK VLFGX UCALX VYMIG MMNMF DXTGN VHVRM MEVOU YFZSL RHDRR XFJWC FHUHM UNZEF RDISI KBGPM YVXUZ".replace(" ", "").lower()
        expected_plaintext = "FEIND LIQEI NFANT ERIEK OLONN EBEOB AQTET XANFA NGSUE DAUSG ANGBA ERWAL DEXEN DEDRE IKMOS TWAER TSNEU STADT".replace(" ", "").lower()
        
        plaintext = enigma.input_string(ciphertext)
        
        self.assertEqual(plaintext, expected_plaintext, "Message decryption failed")

if __name__ == '__main__':
    unittest.main()
