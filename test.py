from enigma.RotorWiringI import RotorWiringI
from enigma.RotorWiringII import RotorWiringII
from enigma.RotorWiringIII import RotorWiringIII
from enigma.PlugboardPassthrough import PlugboardPassthrough
from enigma.ReflectorUKWB import ReflectorUKWB
from enigma.EnigmaThreeRotors import EnigmaThreeRotors
from enigma.EtwPassthrough import EtwPassthrough

plugboard = PlugboardPassthrough()
rotor1 = RotorWiringI(0)
rotor2 = RotorWiringII(0)
rotor3 = RotorWiringIII(0)
reflector = ReflectorUKWB()
etw = EtwPassthrough()

enigma = EnigmaThreeRotors(plugboard,rotor1,rotor2,rotor3,reflector,etw)

if enigma.input_char("a") != 'n':
    print("Error")

rotor1.set_position(1)

if enigma.input_char("a") != 'f':
    print("Error")

rotor2.set_position(1)

if enigma.input_char("a") != 'm':
    print("Error")
    
rotor3.set_position(1)

if enigma.input_char("a") != 'y':
    print("Error")

rotor3.set_position(25)

if enigma.input_char("a") != 's':
    print("Error")

rotor1.set_position(25)
rotor2.set_position(25)

if enigma.input_char("a") != 'f':
    print("Error")

if enigma.input_char("z") != 't':
    print("Error")

rotor2.set_position(300)

if enigma.input_char("z") != 'q':
    print("Error")

if enigma.input_char("q") != 'z':
    print("Error")



# print(plugboard)
#print(rotor1)
#print(rotor2)
#print(rotor3)
# print(reflector)

#rotor2.increment_position()


