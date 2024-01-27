from Observer import Observer
from string import ascii_lowercase
import logging


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
        ## Triggering rotors extra rotation due to double step issue
        for rotor in self.rotors:
            ## Rotor extra rotation should be done only if it's triggered by double step issue and if the rotor is not the last one in the list
            if rotor.double_step_triggered == True and self.rotors.index(rotor) < len(self.rotors)-1:
                    rotor.increment_position()
                    rotor.double_step_triggered = False
        if self.auto_increment_rotors == True:
            self.rotors[0].increment_position()
        scrambled_char = self.process_char(char)
        return scrambled_char           

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
        scrambled_char = self.plugboard.switch_char(scrambled_char)
        logging.debug("Scrambled letter from plugboard: {}".format(scrambled_char))
        logging.info("Scrambled letter to lamp: {}".format(scrambled_char))
        return scrambled_char
    
    def update(self, observable, *args, **kwargs):
        # If there is rotor N+1, increment its position by 1
        if observable in self.rotors and self.rotors.index(observable) < len(self.rotors)-1:
            self.rotors[self.rotors.index(observable)+1].increment_position()
            # Engaging the enigma double step issue, only if the next rotor is not the last in the array
            if self.rotors[self.rotors.index(observable)+1].position in self.rotors[self.rotors.index(observable)+1].notch_indexes:
                self.rotors[self.rotors.index(observable)+1].double_step_triggered = True
        
        
    
    @staticmethod        
    def shift_letter(letter,shift):
	    return Enigma.alphabet[(Enigma.alphabet.index(letter)+shift) % len(Enigma.alphabet)]



