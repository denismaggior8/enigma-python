
# Import from enigma module
from RotorWiringI import RotorWiringI
from RotorWiringII import RotorWiringII
from RotorWiringIII import RotorWiringIII
from PlugboardPassthrough import PlugboardPassthrough
from ReflectorUKWB import ReflectorUKWB
from EnigmaThreeRotors import EnigmaThreeRotors
from EtwPassthrough import EtwPassthrough

# Import from python ecosystem
import logging
import sys

# Setup Enigma components
plugboard = PlugboardPassthrough()
rotor1 = RotorWiringI(0)
rotor2 = RotorWiringII(0)
rotor3 = RotorWiringIII(0)
reflector = ReflectorUKWB()
etw = EtwPassthrough()

# Setup Enigma machine
enigma = EnigmaThreeRotors(plugboard,rotor1,rotor2,rotor3,reflector,etw)

# Configure logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# Test the Enigma machine
if __name__ == "__main__":
   print(enigma.input_char("a"))
   enigma.rotors[0].increment_position()
   print(enigma.input_char("a"))
