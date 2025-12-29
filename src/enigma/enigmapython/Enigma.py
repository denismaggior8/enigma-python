from .Observer import Observer
from .RotatingReflector import RotatingReflector
from .Alphabets import Alphabets
from .Journaled import Journaled
from .Clonable  import Clonable
from .Utils import Utils
import logging


class Enigma(Observer,Journaled,Clonable):
    
    plugboard = None
    rotors = None
    reflector = None
    etw = None
    auto_increment_rotors = False

    alphabet_list = None

    def add_rotor(self,idx,rotor):
        if self.auto_increment_rotors == True and rotor is not None:
            rotor.add_observer(self)
        self.rotors[idx] = rotor

    def __init__(self, plugboard, rotors, reflector,etw,auto_increment_rotors=False, alphabet=Alphabets.lookup.get("latin_i18n_26chars_lowercase")):
        Journaled.__init__(self)
        Clonable.__init__(self)
        self.plugboard = plugboard
        self.reflector = reflector
        self.rotors = [None]*len(rotors)
        self.etw = etw
        self.auto_increment_rotors = auto_increment_rotors
        self.alphabet_list = list(alphabet)
        for i, rotor in enumerate(rotors):
            self.add_rotor(i, rotor)
        

    def input_string(self,str):
        output_string = ""
        for char in str:
            output_string += self.input_char(char)
        return output_string

    def input_char(self,char):
        char = char.lower()
        logging.info("Input char: {}".format(char))
        ## Triggering rotors extra rotation due to double step issue
        for rotor in self.rotors:
            ## Rotor extra rotation should be done only if it's not the last one in the list
            if rotor.double_step_triggered == True and self.rotors.index(rotor) < len(self.rotors)-1:
                    rotor.increment_position()
                    rotor.double_step_triggered = False
            if isinstance(self.reflector, RotatingReflector) and self.reflector.double_step_triggered == True:
                self.reflector.increment_position()
                self.reflector.double_step_triggered = False
        if self.auto_increment_rotors == True:
            self.rotors[0].increment_position()
        scrambled_char = self.process_char(char)
        super().append_to_journal({
            'input_char': char,
            'output_char': scrambled_char
        })
        return scrambled_char           

    """
         UKW   Rotor  Rotor  Rotor   ETW  PLUGBOARD
                 N      2      1      
         ___    ___    ___    ___    ___    ___
        |   |  |   |  |   |  |   |  |   |  |   |
        |  -|--|---|--|---|--|---|--|---|--|---|-- < Key
        | | |  |   |  |   |  |   |  |   |  |   |
        | | |  |   |  |   |  |   |  |   |  |   |
        |  -|--|---|--|---|--|---|--|---|--|---|-- > Lamp
        |   |  |   |  |   |  |   |  |   |  |   |
         ---    ---    ---    ---    ---    ---
    """
    def process_char(self, char):
        scrambled_char = self.plugboard.scramble_char(self.plugboard.wiring,self.plugboard.alphabet_list.index(char),0)
        logging.debug("Scrambled letter from plugboard: {}".format(scrambled_char))
        
        # Calculate inverted wiring for ETW
        inverted_wiring = Utils.inverse_string_permutation(self.etw.wiring, ''.join(self.etw.alphabet_list))
        
        scrambled_char = self.etw.scramble_char(inverted_wiring, self.alphabet_list.index(scrambled_char), 0)
        logging.debug("Scrambled letter from ETW: {}".format(scrambled_char))
        iteration = 0
        for rotor in self.rotors:
            if iteration == 0:
                scrambled_char = rotor.scramble_char(rotor.wiring,self.alphabet_list.index(scrambled_char), rotor.position)
            else:
                scrambled_char = rotor.scramble_char(rotor.wiring,self.alphabet_list.index(scrambled_char)-self.rotors[iteration-1].position, rotor.position) 
            iteration +=1
            logging.debug("Scrambled letter from rotor{}: {}".format(str(iteration),scrambled_char))
        reflector_pos = getattr(self.reflector, 'position', 0)
        scrambled_char = self.reflector.scramble_char(self.reflector.wiring,(self.alphabet_list.index(scrambled_char)-self.rotors[iteration-1].position), reflector_pos)
        logging.debug("Scrambled letter from reflector: {}".format(scrambled_char))
        
        # Adjust for reflector position on return path
        if reflector_pos != 0:
            scrambled_char = self.shift_letter(scrambled_char, -reflector_pos, self.alphabet_list)
            
        for rotor in reversed(self.rotors):
            if iteration == len(self.rotors):
                scrambled_char = rotor.scramble_char(self.alphabet_list,(rotor.wiring.index(self.shift_letter(scrambled_char,rotor.position,self.alphabet_list))-rotor.position), rotor.position)
            else:
                scrambled_char = rotor.scramble_char(self.alphabet_list,(rotor.wiring.index(self.shift_letter(scrambled_char, (rotor.position - self.rotors[iteration].position),self.alphabet_list)) - rotor.position), rotor.position)
            iteration -=1
            logging.debug("Scrambled letter from rotor{}: {}".format(str(iteration+1),scrambled_char))   
        
        # Processing rotor 1 returning signal by ETW
        scrambled_char = self.etw.scramble_char(self.alphabet_list,(inverted_wiring.index(self.shift_letter(scrambled_char, (0 - self.rotors[iteration].position),self.alphabet_list))), 0)
        logging.debug("Scrambled letter from ETW: {}".format(scrambled_char))
        
        scrambled_char = self.plugboard.scramble_char(self.plugboard.wiring,self.plugboard.alphabet_list.index(scrambled_char),0)
        logging.debug("Scrambled letter from plugboard: {}".format(scrambled_char))
        logging.info("Scrambled letter to lamp: {}".format(scrambled_char))
        return scrambled_char
    
    def update(self, observable, *args, **kwargs):
        # If there is rotor N+1, increment its position by 1
        if observable in self.rotors and self.rotors.index(observable) < len(self.rotors)-1:
            self.rotors[self.rotors.index(observable)+1].increment_position()
            logging.debug("Rotor at index {} has been incremented by 1 position".format(self.rotors.index(observable)+1))
            # Engaging the enigma double step issue, only if the next rotor position is in its notch indexe/s
            if self.rotors[self.rotors.index(observable)+1].position in self.rotors[self.rotors.index(observable)+1].turnover_indexes:
                self.rotors[self.rotors.index(observable)+1].double_step_triggered = True
        # If the rotor is the last one in the list, but the machine has a rotating reflector, increment its position by 1
        if observable in self.rotors and self.rotors.index(observable) == len(self.rotors)-1 and isinstance(self.reflector, RotatingReflector):
            self.reflector.increment_position()
            logging.debug("Reflector has been incremented by 1 position")
            # Engaging the enigma double step issue, only if the next rotor position is in its notch indexe/s
            if self.reflector.position in self.reflector.turnover_indexes:
                self.reflector.double_step_triggered = True
        
    @staticmethod        
    def shift_letter(letter,shift,alphabet_list):
        return alphabet_list[(alphabet_list.index(letter)+shift) % len(alphabet_list)]
    
    def clone(self):
        new_enigma = super().clone()
        for rotor in new_enigma.rotors:
                rotor.add_observer(new_enigma)
        return new_enigma