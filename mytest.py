# Import from enigma module
from EnigmaM3RotorVI import EnigmaM3RotorVI
from EnigmaM3RotorII import EnigmaM3RotorII
from EnigmaM3RotorIII import EnigmaM3RotorIII
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
rotor1 = EnigmaM3RotorVI(0)
rotor2 = EnigmaM3RotorII(0)
rotor3 = EnigmaM3RotorIII(0)
reflector = ReflectorUKWB()
etw = EtwPassthrough()

# Setup Enigma machine
enigma = EnigmaM3(plugboard, rotor1, rotor2, rotor3, reflector, etw, True)

# Configure logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Test the Enigma machine
if __name__ == "__main__":
    text = ""
    for i in range(0, ((26 * 13) * 13)):
        text += "d"
    print(text)
