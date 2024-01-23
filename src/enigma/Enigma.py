from RotorWiringI import RotorWiringI
from RotorWiringII import RotorWiringII
from RotorWiringIII import RotorWiringIII
from PlugboardPassthrough import PlugboardPassthrough
from ReflectorUKWB import ReflectorUKWB
from EtwPassthrough import EtwPassthrough
from Observer import Observer
from string import ascii_lowercase
import logging
import unittest

class Enigma(Observer):
    
    plugboard = None
    rotors = None
    reflector = None
    etw = None
    auto_increment_rotors = False

    alphabet = list(ascii_lowercase)

    def __init__(self, plugboard, rotors, reflector,etw,auto_increment_rotors=False):
        self.plugboard = plugboard
        self.rotors = rotors
        self.reflector = reflector
        self.etw = etw
        self.auto_increment_rotors = auto_increment_rotors
        if auto_increment_rotors == True:
            for rotor in rotors:
                rotor.add_observer(self)

    def input_string(self,str):
        output_string = ""
        for char in str:
            output_string += self.input_char(char)
        return output_string

    def input_char(self,char):
        logging.info("Input char: {}".format(char))
        if self.auto_increment_rotors == True:
            self.rotors[0].increment_position()
        return self.process_char(char)

    def process_char(self, char):
        scrambled_char = self.plugboard.switch_char(char)
        logging.debug("Scrambled letter from plugboard: {}".format(scrambled_char))
        iteration = 0
        for rotor in self.rotors:
            if iteration == 0:
                scrambled_char = rotor.scramble_letter_index(rotor.wiring,Enigma.alphabet.index(scrambled_char))
            else:
                scrambled_char = rotor.scramble_letter_index(rotor.wiring,Enigma.alphabet.index(scrambled_char)-self.rotors[iteration-1].position) 
            iteration +=1
            logging.debug("Scrambled letter from rotor{}: {}".format(str(iteration),scrambled_char))
        scrambled_char = self.reflector.scramble_letter_index(self.reflector.wiring,(Enigma.alphabet.index(scrambled_char)-self.rotors[iteration-1].position))
        logging.debug("Scrambled letter from reflector: {}".format(scrambled_char))
        for rotor in reversed(self.rotors):
            if iteration == len(self.rotors):
                scrambled_char = rotor.scramble_letter_index(Enigma.alphabet,(rotor.wiring.index(Enigma.shift_letter(scrambled_char,rotor.position))-rotor.position))
            else:
                scrambled_char = rotor.scramble_letter_index(Enigma.alphabet,(rotor.wiring.index(Enigma.shift_letter(scrambled_char, (rotor.position - self.rotors[iteration].position))) - rotor.position))
            iteration -=1
            logging.debug("Scrambled letter from rotor{}: {}".format(str(iteration+1),scrambled_char))   
        scrambled_char = self.etw.switch_char(scrambled_char,-self.rotors[iteration].position)
        
       
        logging.debug("Scrambled letter from ETW: {}".format(scrambled_char))
        logging.info("Scrambled letter to lamp: {}".format(scrambled_char))
        return scrambled_char
    
    def update(self, observable, *args, **kwargs):
        if self.rotors.index(observable) != None and self.rotors.index(observable) < len(self.rotors):
          self.rotors[self.rotors.index(observable)+1].increment_position()
    
    @staticmethod        
    def shift_letter(letter,shift):
	    return Enigma.alphabet[(Enigma.alphabet.index(letter)+shift) % len(Enigma.alphabet)]



class TestEnigma(unittest.TestCase):
     
    def test_enigma_3_rotors_output(self):
        plugboard = PlugboardPassthrough()
        rotor1 = RotorWiringI(25)
        rotor2 = RotorWiringII(25)
        rotor3 = RotorWiringIII(25)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = Enigma(plugboard,[rotor1, rotor2, rotor3],reflector,etw)
        self.assertEqual(enigma.input_char("z"),"t","Enigma output error")

    def test_enigma_3_rotors_output_reverted(self):
        plugboard = PlugboardPassthrough()
        rotor1 = RotorWiringI(25)
        rotor2 = RotorWiringII(25)
        rotor3 = RotorWiringIII(25)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = Enigma(plugboard,[rotor1, rotor2, rotor3],reflector,etw)
        scrambled_char = enigma.input_char("z")
        self.assertEqual(enigma.input_char(scrambled_char),"z","Enigma output error")

    def test_enigma_3_rotors_automatic_rotor_rotation(self):
        plugboard = PlugboardPassthrough()
        rotor1 = RotorWiringI(0)
        rotor2 = RotorWiringII(0)
        rotor3 = RotorWiringIII(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = Enigma(plugboard,[rotor1, rotor2, rotor3],reflector,etw,True)
        for i in range(len(rotor1.wiring)):
           enigma.input_char("a")
        self.assertEqual(rotor1.position,0,"Enigma output error")
        self.assertEqual(rotor1.rotations_counter,0,"Enigma output error")
        #self.assertEqual(rotor2.position,1,"Enigma output error")
        #self.assertEqual(rotor1.rotations_counter,0,"Enigma output error")
        #self.assertEqual(rotor3.position,0,"Enigma output error")
        #self.assertEqual(rotor3.rotations_counter,0,"Enigma output error")
        #for i in range(len(rotor1.wiring)*len(rotor2.wiring)):
        #   enigma.input_char("a")
        #print(rotor2.position)
        #print(rotor2.rotations_counter)

    def test_enigma_3_encrypt_string(self):
        plugboard = PlugboardPassthrough()
        rotor1 = RotorWiringI(0)
        rotor2 = RotorWiringII(0)
        rotor3 = RotorWiringIII(0)
        reflector = ReflectorUKWB()
        etw = EtwPassthrough()
        enigma = Enigma(plugboard,[rotor1, rotor2, rotor3],reflector,etw,True)
        encrypted_string = enigma.input_string("ciao")
        self.assertEqual(encrypted_string,"pqzz","Enigma encryption error")

if __name__ == "__main__":
    unittest.main()