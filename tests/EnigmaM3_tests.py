from enigmapython.EnigmaM3RotorI import EnigmaM3RotorI
from enigmapython.EnigmaM3RotorII import EnigmaM3RotorII
from enigmapython.EnigmaM3RotorIII import EnigmaM3RotorIII
from enigmapython.EnigmaM3RotorIV import EnigmaM3RotorIV
from enigmapython.EnigmaM3RotorV import EnigmaM3RotorV
from enigmapython.EnigmaM3RotorVI import EnigmaM3RotorVI
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.ReflectorUKWB import ReflectorUKWB
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaM3 import EnigmaM3
from enigma.machine import EnigmaMachine
from string import ascii_lowercase
import random
import logging
import unittest
import sys

class TestEnigmaM3(unittest.TestCase):
     
    def test_enigma_3_rotors_output(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(25)
        rotor2 = EnigmaM3RotorII(25)
        rotor3 = EnigmaM3RotorIII(25)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw)
        self.assertEqual(enigma.input_char("z"),"t","Enigma output error")

    def test_enigma_3_rotors_output_reversed(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(25)
        rotor2 = EnigmaM3RotorII(25)
        rotor3 = EnigmaM3RotorIII(25)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw)
        scrambled_char = enigma.input_char("z")
        self.assertEqual(enigma.input_char(scrambled_char),"z","Enigma output error")

    def test_enigma_3_rotors_automatic_rotation(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(0)
        rotor2 = EnigmaM3RotorII(0)
        rotor3 = EnigmaM3RotorIII(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw,True)
        # Cypher 34 charachters
        for i in range(1,35):
           enigma.input_char("a")
        # Rotor1 position should be 'i', indexed by 8    
        self.assertEqual(rotor1.position,8,"Rotor position error")
        # Rotor1 should have done 34 rotations    
        self.assertEqual(rotor1.rotations_counter,34,"Rotor rotations error")
        # Rotor2 position should be 'b', indexed by 1    
        self.assertEqual(rotor2.position,1,"Rotor position error")
        # Rotor2 should have done 1 rotations    
        self.assertEqual(rotor2.rotations_counter,1,"Rotor rotations error")

    def test_enigma_3_rotors_boundaries(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(26)
        rotor2 = EnigmaM3RotorII(26)
        rotor3 = EnigmaM3RotorIII(26)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw,True)
        enigma.input_char("a")
        self.assertEqual(rotor1.position,1,"Rotor rotations error")
        self.assertEqual(rotor2.position,0,"Rotor rotations error")
        self.assertEqual(rotor3.position,0,"Rotor rotations error")

    #def test_enigma_3_rotors_complete_rotations(self):
    #    plugboard = PlugboardPassthrough()
    #    rotor1 = EnigmaM3RotorI(0)
    #    rotor2 = EnigmaM3RotorII(0)
    #    rotor3 = EnigmaM3RotorIII(0)
    #    reflector = ReflectorUKWB()
    #    etw = EtwPassthrough()
    #    enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw,True)
    #    # Cypher 17577 charachters
    #    for i in range(1,17577):
    #       enigma.input_char("a")
    #    self.assertEqual(rotor1.position,0,"Rotor rotations error")
    #    self.assertEqual(rotor2.position,0,"Rotor rotations error")
    #    self.assertEqual(rotor3.position,0,"Rotor rotations error")
    
    def test_enigma_3_rotors_first_to_second_rotor_rotation(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(0)
        rotor2 = EnigmaM3RotorII(0)
        rotor3 = EnigmaM3RotorIII(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw,True)
        for i in range(1,18):
           enigma.input_char("a")
        self.assertEqual(rotor1.position,17,"Rotor rotations error")
        self.assertEqual(rotor2.position,1,"Rotor rotations error")
    

    def test_enigma_3_rotors_encrypt_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(0)
        rotor2 = EnigmaM3RotorII(0)
        rotor3 = EnigmaM3RotorIII(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw,True)
        encrypted_string = enigma.input_string("ciao")
        self.assertEqual(encrypted_string,"pqzz","Enigma encryption error")
    
    def test_enigma_3_rotors_inverted_encrypt_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorIII(0)
        rotor2 = EnigmaM3RotorII(0)
        rotor3 = EnigmaM3RotorI(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw,True)
        encrypted_string = enigma.input_string("ciao")
        self.assertEqual(encrypted_string,"qozm","Enigma encryption error")

    def test_enigma_3_rotors_encrypt_long_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(0)
        rotor2 = EnigmaM3RotorII(0)
        rotor3 = EnigmaM3RotorIII(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw,True)
        encrypted_string = enigma.input_string("supercalifragilistichespiralidoso")
        self.assertEqual(encrypted_string,"xbbdugsoaoywaobzgkcggrdenwmeqnxap","Enigma encryption error")
    
    def test_enigma_3_rotors_encrypt_very_long_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(0)
        rotor2 = EnigmaM3RotorII(0)
        rotor3 = EnigmaM3RotorIII(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw,True)
        encrypted_string = enigma.input_string("supercalifragilistichespiralidososupercalifragilistichespiralidoso")
        self.assertEqual(encrypted_string,"xbbdugsoaoywaobzgkcggrdenwmeqnxapvwykgzuqpiwdiprbwzmiqxngbbrivrbue","Enigma encryption error")

    def test_enigma_3_rotors_encrypt_very_long_string_reversed(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(0)
        rotor2 = EnigmaM3RotorII(0)
        rotor3 = EnigmaM3RotorIII(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw,True)
        encrypted_string = enigma.input_string("xbbdugsoaoywaobzgkcggrdenwmeqnxapvwykgzuqpiwdiprbwzmiqxngbbrivrbue")
        self.assertEqual(encrypted_string,"supercalifragilistichespiralidososupercalifragilistichespiralidoso","Enigma encryption error")

    def test_enigma_3_rotors_inverted_encrypt_very_long_string_reversed(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorIII(0)
        rotor2 = EnigmaM3RotorII(0)
        rotor3 = EnigmaM3RotorI(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw,True)
        encrypted_string = enigma.input_string("jvswemcgjqvshqvkuidiwplsxjyomqgflhcnsulnyxzcufozgxbqqsyghxkcrtjzbd")
        self.assertEqual(encrypted_string,"supercalifragilistichespiralidososupercalifragilistichespiralidoso","Enigma encryption error")

    def test_enigma_3_rotors_III_IV_V(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorIII(0)
        rotor2 = EnigmaM3RotorIV(0)
        rotor3 = EnigmaM3RotorV(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw,True)
        encrypted_string = enigma.input_string("thisismyawesomeenigma")
        self.assertEqual(encrypted_string,"yoaftqlkbpjwtwvjukoif","Enigma encryption error")

    def test_enigma_3_rotors_IV_V_VI_positions_0(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorIV(0)
        rotor2 = EnigmaM3RotorV(0)
        rotor3 = EnigmaM3RotorVI(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw,True)
        encrypted_string = enigma.input_string("thisismyawesomeenigmasupercalifragilistichespiralidososupercalifragilistichespiralidoso")
        self.assertEqual(encrypted_string,"gbnwtwckrfhpeubluyzpihridbumokuadszsxqjfubildqzwtqettxlxxcotdsmxupanfpwephanborbymwswqy","Enigma encryption error")

    def test_enigma_3_rotors_IV_V_VI_different_positions(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorIV(25)
        rotor2 = EnigmaM3RotorV(4)
        rotor3 = EnigmaM3RotorVI(15)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw,True)
        encrypted_string = enigma.input_string("thisismyawesomeenigmasupercalifragilistichespiralidososupercalifragilistichespiralidoso")
        self.assertEqual(encrypted_string,"grdftnwtlegogzglhwbjgttnnwaigcpamesxheqjtxiecywvdxcncyifitbpgokalupxaambtxblvkmjlgejgdv","Enigma encryption error")

   #def test_enigma_3_rotors_IV_V_VI_complete_rotations(self):
   #    plugboard = PlugboardPassthrough()
   #    rotor1 = EnigmaM3RotorIV(0)
   #    rotor2 = EnigmaM3RotorV(0)
   #    rotor3 = EnigmaM3RotorVI(0)
   #    reflector = ReflectorUKWB()
   #    etw = EtwPassthrough()
   #    enigma = EnigmaM3(plugboard,rotor1, rotor2, rotor3,reflector,etw,True)
   #    # Cypher 17577 charachters
   #    for i in range(1,17577):
   #       enigma.input_char("a")
   #    self.assertEqual(rotor1.position,0,"Rotor rotations error")
   #    self.assertEqual(rotor2.position,0,"Rotor rotations error")
   #    self.assertEqual(rotor3.position,0,"Rotor rotations error")

    def test_enigma_3_rotors_VI_VI_VI_rotations(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorVI(0)
        rotor2 = EnigmaM3RotorVI(0)
        rotor3 = EnigmaM3RotorVI(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor1, rotor2, rotor3, reflector, etw, True)
        # Cypher 26 charachters
        for i in range(1, 27):
            enigma.input_char("a")
        self.assertEqual(rotor1.position, 0, "Rotor rotations error")
        self.assertEqual(rotor2.position, 2, "Rotor rotations error")
        self.assertEqual(rotor3.position, 0, "Rotor rotations error")

    #def test_enigma_3_rotors_VI_VI_VI_complete_rotations(self):
    #    plugboard = PlugboardPassthrough()
    #    rotor1 = EnigmaM3RotorVI(0)
    #    rotor2 = EnigmaM3RotorVI(0)
    #    rotor3 = EnigmaM3RotorVI(0)
    #    reflector = ReflectorUKWB()
    #    etw = EtwPassthrough()
    #    enigma = EnigmaM3(plugboard, rotor1, rotor2, rotor3, reflector, etw, True)
    #    # Cypher 26 charachters
    #    for i in range(0, (26*13)*13):
    #        enigma.input_char("a")
    #    self.assertEqual(rotor1.position, 0, "Rotor rotations error")
    #    self.assertEqual(rotor2.position, 0, "Rotor rotations error")
    #    self.assertEqual(rotor3.position, 0, "Rotor rotations error")
    
    #def test_enigma_3_rotors_VI_VI_VI_rotations(self):
    #    plugboard = PlugboardPassthrough()
    #    rotor1 = EnigmaM3RotorVI(0)
    #    rotor2 = EnigmaM3RotorVI(0)
    #    rotor3 = EnigmaM3RotorVI(0)
    #    reflector = ReflectorUKWB()
    #    etw = EtwPassthrough()
    #    enigma = EnigmaM3(plugboard, rotor1, rotor2, rotor3, reflector, etw, True)
    #    # Cypher 26 charachters
    #    for i in range(0, (26*13)):
    #        enigma.input_char("a")
    #    self.assertEqual(rotor1.position, 0, "Rotor rotations error")
    #    self.assertEqual(rotor2.position, 0, "Rotor rotations error")
    #    self.assertEqual(rotor3.position, 2, "Rotor rotations error")
    
    def test_enigma_3_rotors_VI_VI_VI_rotations_from_0_very_long_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorVI(0)
        rotor2 = EnigmaM3RotorVI(0)
        rotor3 = EnigmaM3RotorVI(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor1, rotor2, rotor3, reflector, etw, True)
        encrypted_string = enigma.input_string("dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
        #print(rotor1.position)
        #print(rotor2.position)
        #print(rotor3.position)
        self.assertEqual(rotor1.position,0, "Rotor position error")
        self.assertEqual(rotor2.position,12, "Rotor position error")
        self.assertEqual(rotor3.position,0, "Rotor position error")
        self.assertEqual(encrypted_string,"nlyzfbxcgczzgzyyzmwkwetytugtatwigjqxetmjfopvnnzioxwxxzyxafgwajtjjqhyfyztfxenfaabfepxpxfcxjpqrhoeembxrqzsbfsaihbunzhcgujhcuazvvrjklqkgrtyvzcsahcuxfaqglhpfqqg","Enigma encryption error")
    
    def test_enigma_3_rotors_III_III_III_rotations_from_0_very_long_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorIII(0)
        rotor2 = EnigmaM3RotorIII(0)
        rotor3 = EnigmaM3RotorIII(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor1, rotor2, rotor3, reflector, etw, True)
        cleartext = 'd' * 100000
        my_encrypted_string = enigma.input_string(cleartext)
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='III III III',
            reflector='B',
            ring_settings=[0, 0, 0],
            plugboard_settings=None)
        other_machine.set_display('AAA')
        other_encrypted_string = other_machine.process_text(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")
    
    def test_enigma_3_rotors_I_II_III_rotations_from_0_very_long_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(0)
        rotor2 = EnigmaM3RotorII(0)
        rotor3 = EnigmaM3RotorIII(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = 'd' * 100000
        my_encrypted_string = enigma.input_string(cleartext)
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='I II III',
            reflector='B',
            ring_settings=[0, 0, 0],
            plugboard_settings=None)
        other_machine.set_display('AAA')
        other_encrypted_string = other_machine.process_text(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")

    def test_enigma_3_rotors_III_II_I_rotations_from_0_very_long_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorIII(0)
        rotor2 = EnigmaM3RotorII(0)
        rotor3 = EnigmaM3RotorI(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = 'd' * 100000
        my_encrypted_string = enigma.input_string(cleartext)
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='III II I',
            reflector='B',
            ring_settings=[0, 0, 0],
            plugboard_settings=None)
        other_machine.set_display('AAA')
        other_encrypted_string = other_machine.process_text(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")

    def test_enigma_3_rotors_III_IV_V_rotations_from_0_very_long_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorV(0)
        rotor2 = EnigmaM3RotorIV(0)
        rotor3 = EnigmaM3RotorIII(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = 'd' * 100000
        my_encrypted_string = enigma.input_string(cleartext)
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='V IV III',
            reflector='B',
            ring_settings=[0, 0, 0],
            plugboard_settings=None)
        other_machine.set_display('AAA')
        other_encrypted_string = other_machine.process_text(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")

    def test_enigma_3_rotors_IV_V_VI_rotations_from_0_very_long_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorVI(0)
        rotor2 = EnigmaM3RotorV(0)
        rotor3 = EnigmaM3RotorIV(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = 'd' * 100000
        my_encrypted_string = enigma.input_string(cleartext)
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='VI V IV',
            reflector='B',
            ring_settings=[0, 0, 0],
            plugboard_settings=None)
        other_machine.set_display('AAA')
        other_encrypted_string = other_machine.process_text(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")

    def test_enigma_3_rotors_IV_V_VI_rotations_from_0_very_long_random_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorVI(0)
        rotor2 = EnigmaM3RotorV(0)
        rotor3 = EnigmaM3RotorIV(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ''.join(random.choice(ascii_lowercase) for i in range(100000))
        my_encrypted_string = enigma.input_string(cleartext)
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='VI V IV',
            reflector='B',
            ring_settings=[0, 0, 0],
            plugboard_settings=None)
        other_machine.set_display('AAA')
        other_encrypted_string = other_machine.process_text(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")


    def test_enigma_3_rotors_VI_VI_VI_rotations_from_0_very_long_random_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorVI(0)
        rotor2 = EnigmaM3RotorVI(0)
        rotor3 = EnigmaM3RotorVI(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ''.join(random.choice(ascii_lowercase) for i in range(100000))
        my_encrypted_string = enigma.input_string(cleartext)
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='VI VI VI',
            reflector='B',
            ring_settings=[0, 0, 0],
            plugboard_settings=None)
        other_machine.set_display('AAA')
        other_encrypted_string = other_machine.process_text(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")


    def test_enigma_3_rotors_I_II_III_rotations_from_0_random_ring_very_long_random_string(self):
        rnd_ring1 = random.randrange(26)
        rnd_ring2 = random.randrange(26)
        rnd_ring3 = random.randrange(26)
        print(rnd_ring1)
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(0,rnd_ring1)
        rotor2 = EnigmaM3RotorII(0,rnd_ring2)
        rotor3 = EnigmaM3RotorIII(0,rnd_ring3)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ''.join(random.choice(ascii_lowercase) for i in range(5))
        my_encrypted_string = enigma.input_string(cleartext)
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='I II III',
            reflector='B',
            ring_settings=[rnd_ring1, rnd_ring2, rnd_ring3],
            plugboard_settings=None)
        other_machine.set_display('AAA')
        other_encrypted_string = other_machine.process_text(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")

    def test_enigma_3_rotors_VI_VI_VI_different_rings_rotations_from_0_very_long_random_string(self):
        rnd_ring1 = random.randrange(26)
        rnd_ring2 = random.randrange(26)
        rnd_ring3 = random.randrange(26)
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorVI(0,rnd_ring1)
        rotor2 = EnigmaM3RotorVI(0,rnd_ring2)
        rotor3 = EnigmaM3RotorVI(0,rnd_ring3)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ''.join(random.choice(ascii_lowercase) for i in range(100000))
        my_encrypted_string = enigma.input_string(cleartext)
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='VI VI VI',
            reflector='B',
            ring_settings=[rnd_ring1, rnd_ring2, rnd_ring3],
            plugboard_settings=None)
        other_machine.set_display('AAA')
        other_encrypted_string = other_machine.process_text(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")

    def test_enigma_3_rotors_I_I_I_resetting_rings_rotations_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(0,4)
        rotor2 = EnigmaM3RotorI(0,2)
        rotor3 = EnigmaM3RotorI(0,6)
        rotor1.set_scrambler_ring(1)
        rotor2.set_scrambler_ring(20)
        rotor3.set_scrambler_ring(8)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = "ciaodenis"
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"tjlvbastc","Enigma encryption error")
    
    def test_enigma_3_rotors_I_II_III_resetting_rings_rotations_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(0,4)
        rotor2 = EnigmaM3RotorII(0,2)
        rotor3 = EnigmaM3RotorIII(0,6)
        rotor1.set_scrambler_ring(1)
        rotor2.set_scrambler_ring(20)
        rotor3.set_scrambler_ring(8)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = "ciaodenis"
        my_encrypted_string = enigma.input_string(cleartext)
        self.assertEqual(my_encrypted_string,"vnignrcvn","Enigma encryption error")

    def test_enigma_3_rotors_I_II_III_resetting_rings_rotations_very_long_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(0,4)
        rotor2 = EnigmaM3RotorII(0,2)
        rotor3 = EnigmaM3RotorIII(0,6)
        rotor1.set_scrambler_ring(1)
        rotor2.set_scrambler_ring(20)
        rotor3.set_scrambler_ring(8)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ''.join(random.choice(ascii_lowercase) for i in range(100000))
        my_encrypted_string = enigma.input_string(cleartext)
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='I II III',
            reflector='B',
            ring_settings=[1, 20, 8],
            plugboard_settings=None)
        other_machine.set_display('AAA')
        other_encrypted_string = other_machine.process_text(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")

    def test_enigma_3_rotors_I_II_III_resetting_rings_rotations_111_very_long_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = EnigmaM3RotorI(1,4)
        rotor2 = EnigmaM3RotorII(1,2)
        rotor3 = EnigmaM3RotorIII(1,6)
        rotor1.set_scrambler_ring(1)
        rotor2.set_scrambler_ring(20)
        rotor3.set_scrambler_ring(8)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = EnigmaM3(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
        cleartext = ''.join(random.choice(ascii_lowercase) for i in range(100000))
        my_encrypted_string = enigma.input_string(cleartext)
        other_machine = EnigmaMachine.from_key_sheet(
            rotors='I II III',
            reflector='B',
            ring_settings=[1, 20, 8],
            plugboard_settings=None)
        other_machine.set_display('BBB')
        other_encrypted_string = other_machine.process_text(cleartext)
        self.assertEqual(my_encrypted_string,other_encrypted_string.lower(),"Enigma encryption error")
        

if __name__ == "__main__":
    unittest.main(verbosity=2)