# Import from this package
from enigmapython.EnigmaM4RotorI import EnigmaM4RotorI
from enigmapython.EnigmaM4RotorII import EnigmaM4RotorII
from enigmapython.EnigmaM4RotorIII import EnigmaM4RotorIII
from enigmapython.EnigmaM4RotorBeta import EnigmaM4RotorBeta
from enigmapython.ReflectorUKWBThin import ReflectorUKWBThin
from enigmapython.SwappablePlugboard import SwappablePlugboard
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaM4 import EnigmaM4

# Import from python ecosystem
import logging
import sys

# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Setup Enigma M4 components
plugboard = SwappablePlugboard()
plugboard.bulk_swap({"a":"c","d":"z"})
rotor1 = EnigmaM4RotorI(0)
rotor2 = EnigmaM4RotorII(0)
rotor3 = EnigmaM4RotorIII(0)
rotor4 = EnigmaM4RotorBeta(0)
reflector = ReflectorUKWBThin()
etw = EtwPassthrough()

# Setup Enigma M4 machine
enigma = EnigmaM4(plugboard, rotor1, rotor2, rotor3, rotor4, reflector, etw, True)

# Test the Enigma machine
if __name__ == "__main__":

   print(enigma.input_char("c"))
   print(enigma.input_char("i"))
   print(enigma.input_char("a"))
   print(enigma.input_char("o"))
   
   print(enigma.input_string("supercalifragilistichespiralidoso"))
