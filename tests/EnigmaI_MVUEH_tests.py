import unittest
from enigmapython.EnigmaIRotorII import EnigmaIRotorII
from enigmapython.EnigmaIRotorV import EnigmaIRotorV
from enigmapython.EnigmaIRotorIII import EnigmaIRotorIII
from enigmapython.ReflectorUKWB import ReflectorUKWB
from enigmapython.SwappablePlugboard import SwappablePlugboard
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaI import EnigmaI

class TestEnigmaIMVUEH(unittest.TestCase):
    """
    Validation test case for the authentic WWII German Army Enigma I message 'MVUEH' (Message Nr. 172).
    
    Historical Context:
    - Date: 10 July 1941, 17:30
    - Sender / Radio Station: Callsign 2ny (SS-Totenkopf Division, Quartermaster / Quartiermeister Ib)
    - Kenngruppe: MVU EH
    - Unbroken for 21 years in Frode Weierud's Crypto Cellar archive (2005-2026).
    - Solved in September 2026 by Carter Leffen using OpenAI's GPT-6 Astra, and verified by Frode Weierud.
    
    Sources:
    - https://mvueh-enigma-solved.carterl.chatgpt.site
    - https://cryptocellar.org/bgac/the-mvueh-break.html

    Settings:
    - Enigma Model: Enigma I
    - Reflector: UKW-B
    - Rotor Order: II V III (Left to Right) -> III is Right (Fast), V is Middle, II is Left (Slow)
    - Ring Settings (Ringstellung): H M F -> Left=H (07), Middle=M (12), Right=F (05) [0-based]
    - Grundstellung (Indicator Key): G T A -> Left=G (06), Middle=T (19), Right=A (00) [0-based]
    - Enciphered Message Key: KCI -> Decrypts to RWD
    - Message Body Starting Position: R W D -> Left=R (17), Middle=W (22), Right=D (03) [0-based]
    - Plugboard (Steckerverbindungen): AC BE DG FH KN MO PR SU TV XZ (10 pairs)
    """

    def _setup_plugboard(self) -> SwappablePlugboard:
        plugboard = SwappablePlugboard()
        pairs = ["ac", "be", "dg", "fh", "kn", "mo", "pr", "su", "tv", "xz"]
        for p in pairs:
            plugboard.swap(p[0], p[1])
        return plugboard

    def _create_enigma_instance(self, left_pos: int, mid_pos: int, right_pos: int) -> EnigmaI:
        # Rotors constructor takes (position, ring)
        # Ring settings: H (7), M (12), F (5)
        rotor_right = EnigmaIRotorIII(right_pos, 5)
        rotor_middle = EnigmaIRotorV(mid_pos, 12)
        rotor_left = EnigmaIRotorII(left_pos, 7)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        plugboard = self._setup_plugboard()
        return EnigmaI(plugboard, rotor_right, rotor_middle, rotor_left, reflector, etw, True)

    def test_mvueh_indicator_decryption(self):
        """
        Tests the decryption of the enciphered message key 'KCI' at the Grundstellung 'GTA' to obtain 'RWD'.
        """
        # Grundstellung: GTA -> G(6), T(19), A(0)
        enigma = self._create_enigma_instance(left_pos=6, mid_pos=19, right_pos=0)
        
        decrypted_key = enigma.input_string("kci")
        self.assertEqual(decrypted_key, "rwd", "Message key decryption from GTA failed")

    def test_mvueh_message_decryption(self):
        """
        Tests the decryption of the 82-character MVUEH ciphertext body at the starting position 'RWD'.
        """
        # Message body starting position: RWD -> R(17), W(22), D(3)
        enigma = self._create_enigma_instance(left_pos=17, mid_pos=22, right_pos=3)
        
        ciphertext = "ICRVSORMCCWQTATYEVFXDBZGGSNXWLPSYWZYTCBSWULRTBZCVGODVJUSLSOOMJQJZSXSEBZPEYMDNXJYTC".lower()
        expected_plaintext = "BTTEUMANGABEDESMARSQWEGESXBEFINDEMIQINXROSENOWROSENOWXSOFORTFUNKANTWORTXWASCHBBSCH".lower()
        
        decrypted = enigma.input_string(ciphertext)
        self.assertEqual(decrypted, expected_plaintext, "MVUEH ciphertext decryption failed")

    def test_mvueh_message_encryption_reciprocity(self):
        """
        Tests that encrypting the plaintext at 'RWD' produces the exact ciphertext (reciprocity of Enigma).
        """
        enigma = self._create_enigma_instance(left_pos=17, mid_pos=22, right_pos=3)
        
        plaintext = "BTTEUMANGABEDESMARSQWEGESXBEFINDEMIQINXROSENOWROSENOWXSOFORTFUNKANTWORTXWASCHBBSCH".lower()
        expected_ciphertext = "ICRVSORMCCWQTATYEVFXDBZGGSNXWLPSYWZYTCBSWULRTBZCVGODVJUSLSOOMJQJZSXSEBZPEYMDNXJYTC".lower()
        
        encrypted = enigma.input_string(plaintext)
        self.assertEqual(encrypted, expected_ciphertext, "MVUEH message encryption reciprocity failed")

    def test_mvueh_full_procedure(self):
        """
        Tests the complete historical procedure:
        1. Decrypt indicator KCI at Grundstellung GTA -> reveals message key RWD.
        2. Set rotor positions to the decrypted key.
        3. Decrypt ciphertext -> reveals full plaintext message.
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        # 1. Decrypt indicator at GTA
        enigma = self._create_enigma_instance(left_pos=alphabet.index("g"), mid_pos=alphabet.index("t"), right_pos=alphabet.index("a"))
        decrypted_key = enigma.input_string("kci")
        self.assertEqual(decrypted_key, "rwd")
        
        # 2. Reset rotor positions to decrypted key (order: right=0, middle=1, left=2)
        enigma.rotors[0].position = alphabet.index(decrypted_key[2]) # D
        enigma.rotors[1].position = alphabet.index(decrypted_key[1]) # W
        enigma.rotors[2].position = alphabet.index(decrypted_key[0]) # R
        
        # 3. Decrypt message
        ciphertext = "ICRVSORMCCWQTATYEVFXDBZGGSNXWLPSYWZYTCBSWULRTBZCVGODVJUSLSOOMJQJZSXSEBZPEYMDNXJYTC".lower()
        expected_plaintext = "BTTEUMANGABEDESMARSQWEGESXBEFINDEMIQINXROSENOWROSENOWXSOFORTFUNKANTWORTXWASCHBBSCH".lower()
        
        plaintext = enigma.input_string(ciphertext)
        self.assertEqual(plaintext, expected_plaintext)

    def test_mvueh_left_rotor_turnover_at_char_72(self):
        """
        Validates the rare mid-message turnover of the left-hand rotor (Rotor II).
        As documented in the break analysis, the middle rotor (Rotor V) reaches
        its turnover notch at letter 71 (position 'Z'), triggering the left rotor
        to step from 'R' (17) to 'S' (18) on letter 72.
        """
        enigma = self._create_enigma_instance(left_pos=17, mid_pos=22, right_pos=3)
        plaintext = "BTTEUMANGABEDESMARSQWEGESXBEFINDEMIQINXROSENOWROSENOWXSOFORTFUNKANTWORTXWASCHBBSCH".lower()

        # Characters 1 to 71: Left rotor must remain at R (17)
        for i in range(71):
            enigma.input_char(plaintext[i])
            self.assertEqual(
                enigma.rotors[2].position, 17,
                f"Left rotor stepped prematurely at character {i + 1}"
            )

        # At character 71: Middle rotor is at 'Z' (25), Right rotor is at 'W' (22)
        self.assertEqual(enigma.rotors[1].position, 25, "Middle rotor should be at 'Z'")

        # Character 72 ('x'): Left rotor must step to 'S' (18)
        enigma.input_char(plaintext[71])
        self.assertEqual(
            enigma.rotors[2].position, 18,
            "Left rotor did not step to 'S' at character 72"
        )

    def test_mvueh_historical_transcript_corrections(self):
        """
        Validates decryption against the original raw handwritten intercept
        as cataloged in Frode Weierud's 2005 archive, demonstrating the 8
        optical/transcription misreadings that prevented earlier cryptanalysis.
        """
        # Original handwritten log transcription (82 letters excluding MVUEH):
        # IDEVS ARMCC NQTAT YEVFC DBZGG SMXWL PSYWZ YTCBS WURRT BZCVG ODVJU SLSOO MJQJZ SXSEB ZPEYM DNXJF TC
        raw_intercept = (
            "IDEVS ARMCC NQTAT YEVFC DBZGG SMXWL PSYWZ YTCBS "
            "WURRT BZCVG ODVJU SLSOO MJQJZ SXSEB ZPEYM DNXJF TC"
        ).replace(" ", "").lower()

        # Corrected ciphertext:
        # ICRVS ORMCC WQTAT YEVFX DBZGG SNXWL PSYWZ YTCBS WULRT BZCVG ODVJU SLSOO MJQJZ SXSEB ZPEYM DNXJY TC
        corrected_ciphertext = (
            "ICRVS ORMCC WQTAT YEVFX DBZGG SNXWL PSYWZ YTCBS "
            "WULRT BZCVG ODVJU SLSOO MJQJZ SXSEB ZPEYM DNXJY TC"
        ).replace(" ", "").lower()

        # The 8 corrected positions (0-based indices):
        # Index 1:  'd' -> 'c' (IDEVS -> ICRVS)
        # Index 2:  'e' -> 'r' (IDEVS -> ICRVS)
        # Index 5:  'a' -> 'o' (ARMCC -> ORMCC)
        # Index 10: 'n' -> 'w' (NQTAT -> WQTAT)
        # Index 19: 'c' -> 'x' (YEVFC -> YEVFX)
        # Index 26: 'm' -> 'n' (SMXWL -> SNXWL)
        # Index 42: 'r' -> 'l' (WURRT -> WULRT)
        # Index 79: 'f' -> 'y' (DNXJF -> DNXJY)
        expected_diffs = [1, 2, 5, 10, 19, 26, 42, 79]
        differences = [i for i in range(len(raw_intercept)) if raw_intercept[i] != corrected_ciphertext[i]]
        self.assertEqual(differences, expected_diffs)

        # Decrypting raw intercept yields plaintext with 8 single-character corruptions
        enigma = self._create_enigma_instance(left_pos=17, mid_pos=22, right_pos=3)
        raw_decrypted = enigma.input_string(raw_intercept)

        # Decrypting corrected ciphertext yields clean plaintext
        enigma_corr = self._create_enigma_instance(left_pos=17, mid_pos=22, right_pos=3)
        clean_decrypted = enigma_corr.input_string(corrected_ciphertext)

        pt_diffs = [i for i in range(len(clean_decrypted)) if raw_decrypted[i] != clean_decrypted[i]]
        self.assertEqual(pt_diffs, expected_diffs)


if __name__ == "__main__":
    unittest.main()
