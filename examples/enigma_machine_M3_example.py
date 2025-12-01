# Import from this package
from enigmapython.EnigmaM3RotorI import EnigmaM3RotorI
from enigmapython.EnigmaM3RotorII import EnigmaM3RotorII
from enigmapython.EnigmaM3RotorIII import EnigmaM3RotorIII
from enigmapython.ReflectorUKWB import ReflectorUKWB
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaM3 import EnigmaM3

# Import from python ecosystem
import logging
import sys

# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Setup Enigma M3 components
plugboard = PlugboardPassthrough()
rotor1 = EnigmaM3RotorI(1,4)
rotor2 = EnigmaM3RotorII(1,2)
rotor3 = EnigmaM3RotorIII(1,6)
reflector = ReflectorUKWB()
etw = EtwPassthrough()

# Setup Enigma M3 machine
enigma = EnigmaM3(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)

# Test the Enigma machine
if __name__ == "__main__":
   
   print(enigma.input_char("c"))
   print(enigma.input_char("i"))
   print(enigma.input_char("a"))
   print(enigma.input_char("o"))
   
   print(enigma.input_string("supercalifragilistichespiralidoso"))
