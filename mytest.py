from enigma.machine import EnigmaMachine
from EnigmaIRotorI import EnigmaIRotorI
from EnigmaISonderRotorII import EnigmaISonderRotorII
from EnigmaISonderRotorIII import EnigmaISonderRotorIII
from PlugboardPassthrough import PlugboardPassthrough
from ReflectorSonderUKW import ReflectorSonderUKW
from EtwPassthrough import EtwPassthrough
from EnigmaISonder import EnigmaISonder
from Rotor import Rotor
from string import ascii_lowercase
import logging
from Utils import Utils


logging.basicConfig(level=logging.INFO)
#plugboard = PlugboardPassthrough()
#rotor1 = EnigmaIRotorI(0)
#rotor2 = EnigmaIRotorI(0)
#rotor2 = EnigmaISonderRotorII(0)
#rotor3 = EnigmaISonderRotorIII(0)
#reflector = ReflectorSonderUKW()
#etw = EtwPassthrough()
#enigma = EnigmaISonder(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
#cleartext = "uadenis"
#my_encrypted_string = enigma.input_string(cleartext)

for sub in Utils.find_all_subclasses(Rotor):
    Rotor.register(sub.tag,sub)

#type(object).
print(Rotor.lookup["I_I"].__module__)
print(Rotor.lookup["I_I"].__name__)
print(Utils.instance_class(Rotor.lookup["I_I"].__module__+"."+Rotor.lookup["I_I"].__name__))
#print(Rotor.lookup["I_I"])
#print(my_encrypted_string)