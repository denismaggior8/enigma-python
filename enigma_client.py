from enigma.RotorWiringI import RotorWiringI
from enigma.RotorWiringII import RotorWiringII
from enigma.RotorWiringIII import RotorWiringIII
from enigma.PlugboardPassthrough import PlugboardPassthrough
from enigma.ReflectorUKWB import ReflectorUKWB
from enigma.EnigmaThreeRotors import EnigmaThreeRotors
from enigma.EtwPassthrough import EtwPassthrough
import logging
import sys

plugboard = PlugboardPassthrough()
rotor1 = RotorWiringI(26)
rotor2 = RotorWiringII(26)
rotor3 = RotorWiringIII(26)
reflector = ReflectorUKWB()
etw = EtwPassthrough()

enigma = EnigmaThreeRotors(plugboard,rotor1,rotor2,rotor3,reflector,etw)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

print(enigma.input_char("z"))

# print(plugboard)
#print(rotor1)
#print(rotor2)
#print(rotor3)
# print(reflector)

#rotor2.increment_position()


