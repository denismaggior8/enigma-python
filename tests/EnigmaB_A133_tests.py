from enigmapython.EnigmaB_A133RotorI import EnigmaB_A133RotorI
from enigmapython.EnigmaB_A133RotorII import EnigmaB_A133RotorII
from enigmapython.EnigmaB_A133RotorIII import EnigmaB_A133RotorIII
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.EnigmaB_A133Etw import EnigmaB_A133Etw
from enigmapython.EnigmaB_A133 import EnigmaB_A133
from enigmapython.ReflectorUKW_EnigmaB_A133 import ReflectorUKW_EnigmaB_A133

import unittest


class TestEnigmaD(unittest.TestCase):
    def test_enigma_B_rotors_I_I_I_small_string(self):
        rotor1 = EnigmaB_A133RotorI()
        rotor2 = EnigmaB_A133RotorI()
        rotor3 = EnigmaB_A133RotorI()
        reflector = ReflectorUKW_EnigmaB_A133()
        etw = EnigmaB_A133Etw()
        enigma = EnigmaB_A133(rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = 'aåäö'
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"pgiu","Enigma encryption error")

    def test_enigma_B_rotors_I_II_III_small_string(self):
        rotor1 = EnigmaB_A133RotorI()
        rotor2 = EnigmaB_A133RotorII()
        rotor3 = EnigmaB_A133RotorIII()
        reflector = ReflectorUKW_EnigmaB_A133()
        etw = EnigmaB_A133Etw()
        enigma = EnigmaB_A133(rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = 'aåäö'
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"ylpe","Enigma encryption error")

    def test_enigma_B_rotors_I_II_III_long_string(self):
        rotor1 = EnigmaB_A133RotorI()
        rotor2 = EnigmaB_A133RotorII()
        rotor3 = EnigmaB_A133RotorIII()
        reflector = ReflectorUKW_EnigmaB_A133()
        etw = EnigmaB_A133Etw()
        enigma = EnigmaB_A133(rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = 'ettbesökpåfavoritkafeetaminaochhennessysteräristandeharshoppatsminkochätitlunchtillsammansdevillgärnataenfikainnandegårhemdebestämmersigföratttabussentillsittfavoritkafekafeetliggerpåenlitengatatiominuterutanförcentrumdetärettgammaltkafesomharfunnitsistansedantaletaminaochhennessysterbrukaroftagåditochfikakafeetärmycketpopulärtdetharalltidtrevligpersonalgottkaffeochmångaolikakakorattväljamellanaminabeställerenkaffeutanmjölkochenkanelbullehennessysterbeställerencappuccinoochencitronkakadesitterpåkafeettillsdetstängerdebestämmersigförattfikatillsammansigennästavecka'
        my_encrypted_string = enigma.input_string(cleartext)
        print(my_encrypted_string)
        self.assertEqual(my_encrypted_string,"xfbzblzpändpunzoaöbxozfyrpzåbbulrxjhvmtäxtlupxlatfjgxepnijddfpoäqdzdgkbxkbåvdzmågiuliegdmåntqhsmlfmbvciplvzjebcfmtåofgpfzgepgohdgåjoetpbxgmllagfxvblziqhxndyhmeduatrgnfpamghhthuzqbådcnzgolädhjäreckxpphebbuämxzixögkxcööbpyjltöqjrirdbyryfbsllfqkmqnpzkmzcävmkyvspssivjnqpzmmsfzlftvtböhpöcpnöäöbvmdlcuptöhxmgdzbitgntågigcxkövrzzidåqnqassäståvrfarhahmpåuibjxnzejxnminnäxssyntqectöpbtmåsodlögqafbtcqqkxtencöluoxirpkbpdciforjdtcmåiyiövalftäpbkifvöhdhfspuöxqryåmöqhnfdbiöxkyppxbfzfotaaäeyäzydhhkoictvbjzrhiåöcoeivophbvänskqzeyädlqåckqvsejemlråqonzlulcpgjkzygåövdstcnmguaczuoxrkek","Enigma encryption error")

if __name__ == "__main__":
    unittest.main(verbosity=2)