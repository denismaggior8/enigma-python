from enigma.machine import EnigmaMachine
from EnigmaISonderRotorI import EnigmaISonderRotorI
from EnigmaISonderRotorII import EnigmaISonderRotorII
from EnigmaISonderRotorIII import EnigmaISonderRotorIII
from PlugboardPassthrough import PlugboardPassthrough
from ReflectorSonderUKW import ReflectorSonderUKW
from EtwPassthrough import EtwPassthrough
from EnigmaISonder import EnigmaISonder
from string import ascii_lowercase
import logging


logging.basicConfig(level=logging.INFO)
plugboard = PlugboardPassthrough()
rotor1 = EnigmaISonderRotorI(0)
rotor2 = EnigmaISonderRotorII(0)
rotor3 = EnigmaISonderRotorIII(0)
reflector = ReflectorSonderUKW()
etw = EtwPassthrough()
enigma = EnigmaISonder(plugboard, rotor3, rotor2, rotor1, reflector, etw, True)
cleartext = "uadenis"
my_encrypted_string = enigma.input_string(cleartext)

print(my_encrypted_string)