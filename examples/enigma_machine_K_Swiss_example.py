from enigmapython.EnigmaKSwissRotorI import EnigmaKSwissRotorI
from enigmapython.EnigmaKSwissRotorII import EnigmaKSwissRotorII
from enigmapython.EnigmaKSwissRotorIII import EnigmaKSwissRotorIII
from enigmapython.ReflectorUKW_EnigmaCommercial import ReflectorUKW_EnigmaCommercial
from enigmapython.EtwQWERTZ import EtwQWERTZ
from enigmapython.EnigmaKSwiss import EnigmaKSwiss
import logging
import sys

# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Setup Rotors (position, ring)
rotor1 = EnigmaKSwissRotorI(0, 0)      # Right rotor
rotor2 = EnigmaKSwissRotorII(0, 0)     # Middle rotor
rotor3 = EnigmaKSwissRotorIII(0, 0)    # Left rotor

# Setup Reflector
reflector = ReflectorUKW_EnigmaCommercial()

# Setup ETW (QWERTZ layout)
etw = EtwQWERTZ()

# Create Enigma K Swiss machine
enigma = EnigmaKSwiss(rotor1, rotor2, rotor3, reflector, etw, True)

# Encrypt a message
plaintext = "helloworld"
ciphertext = enigma.input_string(plaintext)

print(f"Plaintext:  {plaintext}")
print(f"Ciphertext: {ciphertext}")

# Reset rotors to initial position for decryption
rotor1.set_position(0)
rotor2.set_position(0)
rotor3.set_position(0)

# Decrypt the message
decrypted = enigma.input_string(ciphertext)
print(f"Decrypted:  {decrypted}")
