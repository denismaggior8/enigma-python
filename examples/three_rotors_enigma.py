
# Import from enigma module
from RotorWiringI import RotorWiringI
from RotorWiringII import RotorWiringII
from RotorWiringIII import RotorWiringIII
from PlugboardPassthrough import PlugboardPassthrough
from ReflectorUKWB import ReflectorUKWB
from EnigmaM3 import EnigmaM3
from EtwPassthrough import EtwPassthrough

# Import from python ecosystem
import logging
import sys
import time

# Setup Enigma components
plugboard = PlugboardPassthrough()
rotor1 = RotorWiringI(0)
rotor2 = RotorWiringII(0)
rotor3 = RotorWiringIII(0)
reflector = ReflectorUKWB()
etw = EtwPassthrough()

# Setup Enigma machine
enigma = EnigmaM3(plugboard,rotor1,rotor2,rotor3,reflector,etw,True)

# Configure logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Test the Enigma machine
if __name__ == "__main__":
   enigma.input_char("c")
   enigma.input_char("i")
   enigma.input_char("a")
   enigma.input_char("o")
   