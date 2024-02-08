# Import from this package
from EnigmaM3RotorI import EnigmaM3RotorI
from EnigmaM3RotorII import EnigmaM3RotorII
from EnigmaM3RotorIII import EnigmaM3RotorIII
from EnigmaM4RotorI import EnigmaM4RotorI
from EnigmaM4RotorII import EnigmaM4RotorII
from EnigmaM4RotorIII import EnigmaM4RotorIII
from EnigmaM4RotorBeta import EnigmaM4RotorBeta
from ReflectorUKWBThin import ReflectorUKWBThin
from PlugboardPassthrough import PlugboardPassthrough
from ReflectorUKWB import ReflectorUKWB
from EnigmaM3 import EnigmaM3
from EnigmaM4 import EnigmaM4
from EtwPassthrough import EtwPassthrough

# Import from python ecosystem
import logging
import sys


# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Setup Enigma M3 components
plugboardM3 = PlugboardPassthrough()
rotor1M3 = EnigmaM3RotorI(1,4)
rotor2M3 = EnigmaM3RotorII(1,2)
rotor3M3 = EnigmaM3RotorIII(1,6)
reflectorM3 = ReflectorUKWB()
etwM3 = EtwPassthrough()

# Setup Enigma M3 machine
enigmaM3 = EnigmaM3(plugboardM3, rotor3M3, rotor2M3, rotor1M3, reflectorM3, etwM3, True)

# Setup Enigma M4 components
plugboardM4 = PlugboardPassthrough()
rotor1M4 = EnigmaM4RotorI(0)
rotor2M4 = EnigmaM4RotorII(0)
rotor3M4 = EnigmaM4RotorIII(0)
rotor4M4 = EnigmaM4RotorBeta(0)
reflectorM4 = ReflectorUKWBThin()
etwM4 = EtwPassthrough()

# Setup Enigma M4 machine
enigmaM4 = EnigmaM4(plugboardM4, rotor1M4, rotor2M4, rotor3M4, rotor4M4, reflectorM4, etwM4, True)

# Setup Enigma M4 machine

# Test the Enigma machines
if __name__ == "__main__":
   
   print(enigmaM3.input_char("c"))
   print(enigmaM3.input_char("i"))
   print(enigmaM3.input_char("a"))
   print(enigmaM3.input_char("o"))
   
   print(enigmaM3.input_string("supercalifragilistichespiralidoso"))

   print(enigmaM4.input_char("c"))
   print(enigmaM4.input_char("i"))
   print(enigmaM4.input_char("a"))
   print(enigmaM4.input_char("o"))
   
   print(enigmaM4.input_string("supercalifragilistichespiralidoso"))