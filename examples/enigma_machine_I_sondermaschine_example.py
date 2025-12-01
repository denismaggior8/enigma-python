# Import from this package
from enigmapython.EnigmaISonderRotorI import EnigmaISonderRotorI
from enigmapython.EnigmaISonderRotorII import EnigmaISonderRotorII
from enigmapython.EnigmaISonderRotorIII import EnigmaISonderRotorIII
from enigmapython.ReflectorSonderUKW import ReflectorSonderUKW
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaISonder import EnigmaISonder

# Import from python ecosystem
import logging
import sys

# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Setup Enigma I Sondermaschine components
plugboard = PlugboardPassthrough()
rotor1 = EnigmaISonderRotorI(ring=0,position=0)
rotor2 = EnigmaISonderRotorII(ring=0,position=0)
rotor3 = EnigmaISonderRotorIII(ring=0,position=0)
reflector = ReflectorSonderUKW()
etw = EtwPassthrough()

# Setup Enigma I Sondermaschine machine
enigma = EnigmaISonder(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)

# Test the Enigma machine
if __name__ == "__main__":
   
   print(enigma.input_char("c"))
   print(enigma.input_char("i"))
   print(enigma.input_char("a"))
   print(enigma.input_char("o"))
   
   print(enigma.input_string("supercalifragilistichespiralidoso"))
