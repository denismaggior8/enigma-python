import unittest
from enigmapython.EnigmaTRotorI import EnigmaTRotorI
from enigmapython.EnigmaTRotorII import EnigmaTRotorII
from enigmapython.EnigmaTRotorIII import EnigmaTRotorIII
from enigmapython.ReflectorUKW_EnigmaT import ReflectorUKW_EnigmaT
from enigmapython.EnigmaTEtw import EnigmaTEtw
from enigmapython.EnigmaT import EnigmaT

class TestEnigmaTTranscript(unittest.TestCase):

    def decrypt_with_finnery_procedure(self, ciphertext, rotors, reflector, etw):
        """
        Helper method to decrypt/encrypt using the 'Finnery' procedure:
        After each group of 5 letters is processed, the reflector (left-most wheel)
        is advanced by one step in the alphabet.
        """
        # Remove spaces/headers to get raw cipher text of A-Z
        cleaned_cipher = "".join([c for c in ciphertext.lower() if c.isalpha()])
        
        enigma = EnigmaT(rotors[0], rotors[1], rotors[2], reflector, etw)
        
        result = []
        # Process in chunks of 5
        for i in range(0, len(cleaned_cipher), 5):
            chunk = cleaned_cipher[i:i+5]
            # Encrypt/Decrypt 5 chars
            decrypted_chunk = enigma.input_string(chunk)
            result.append(decrypted_chunk)
            
            # Move reflector 1 step by hand
            reflector.set_position((reflector.position + 1) % 26)
            
        return "".join(result)

    def test_finnery_procedure_simulation(self):
        # Setup separate objects for encryption to avoid shared observer/stepping state leaks
        rotor1_enc = EnigmaTRotorI(position=0, ring=0)
        rotor2_enc = EnigmaTRotorII(position=0, ring=0)
        rotor3_enc = EnigmaTRotorIII(position=0, ring=0)
        reflector_enc = ReflectorUKW_EnigmaT(position=0, ring=0)
        etw_enc = EnigmaTEtw()

        # Some text longer than 5 chars to trigger reflector stepping
        plaintext = "thisisalongertexttoverifyfinneryprocedure"
        
        # Symmetrical encryption
        ciphertext = self.decrypt_with_finnery_procedure(
            plaintext, 
            [rotor1_enc, rotor2_enc, rotor3_enc], 
            reflector_enc, 
            etw_enc
        )
        
        # Separate objects for decryption
        rotor1_dec = EnigmaTRotorI(position=0, ring=0)
        rotor2_dec = EnigmaTRotorII(position=0, ring=0)
        rotor3_dec = EnigmaTRotorIII(position=0, ring=0)
        reflector_dec = ReflectorUKW_EnigmaT(position=0, ring=0)
        etw_dec = EnigmaTEtw()
        
        # Decrypt
        decrypted = self.decrypt_with_finnery_procedure(
            ciphertext, 
            [rotor1_dec, rotor2_dec, rotor3_dec], 
            reflector_dec, 
            etw_dec
        )
        
        self.assertEqual(decrypted, plaintext, "Symmetric encryption/decryption with Finnery procedure failed")

    def test_original_transcript_placeholder(self):
        # Original Transcript Message A from: https://cryptocellar.org/bgac/enigma-t-messages.html
        # DAN C" C" 6 March 1944 1814/6/27 51
        ciphertext_a = (
            "HCHFZ JIISW NXFZQ JOHCG TSWYI FBHKD TJLJH XLHQT NZEXR YLIAE XHQHW LAYXW KGDRX FLDPC "
            "PYLSE XEBDP HPQTY YEKHN RGZVX XNZHP XGQPL ACDKI VUPGV NUSUZ HALMB ACBHI LVYVC HNOYU "
            "XIACT IVVKG UJEPJ BOJHX KHTFQ ZVVTZ VBDDA MLVPS ZMJCU AZMWU WSAXF ZVPUF LULIF EZATT "
            "ASOLY JRDVP HYVRE GSBBV OQJMN YPUMA IQWQJ"
        )
        
        # Original Transcript Message B from: https://cryptocellar.org/bgac/enigma-t-messages.html
        # DAN C" C" 6 March 1944 1947/6/28 51
        ciphertext_b = (
            "DJYQT FKCHD JEBKM QZDFY QLHCP TLKUL RYIAA BDGEJ XWDBY BABMH LSVLF NCSUA BNBKW BRNRP "
            "XZOKE UJDLO QYYGV ZGHXG IGJLO ODTRC SQQOO GTBET RNGUP IVWGF JNGBW MISQY KVYJI GCTYO "
            "YLWWC CXFPM IKVHQ RRBJA ZLZAE SAMPF BJXOT QOYGQ TYQEI NHZYQ ZCWOP XBOUJ AOEIV GGJKG "
            "MKHNB PQKBI ZNVEH GENJU MNGEI FGJXU UMWRC"
        )
        
        # This is a template test. Once exact daily keys (rotors, positions, rings)
        # from "Breaking 'Tirpitz'" paper are obtained, they can be plugged here.
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)
