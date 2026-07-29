from enigmapython.EnigmaTRotorI import EnigmaTRotorI
from enigmapython.EnigmaTRotorII import EnigmaTRotorII
from enigmapython.EnigmaTRotorIII import EnigmaTRotorIII
from enigmapython.ReflectorUKW_EnigmaT import ReflectorUKW_EnigmaT
from enigmapython.EnigmaTEtw import EnigmaTEtw
from enigmapython.EnigmaT import EnigmaT
import logging
import sys

# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Setup Rotors (position, ring)
# Using Rotors I, II, III for this example
rotor1 = EnigmaTRotorI(0, 0)      # Right rotor (Fast)
rotor2 = EnigmaTRotorII(0, 0)     # Middle rotor
rotor3 = EnigmaTRotorIII(0, 0)    # Left rotor (Slow)

# Setup Reflector
reflector = ReflectorUKW_EnigmaT()

# Setup ETW (Enigma T specific layout)
etw = EnigmaTEtw()

# Create Enigma T machine (Tirpitz - no plugboard)
enigma = EnigmaT(rotor1, rotor2, rotor3, reflector, etw, True)

# Encrypt a message
plaintext = "helloworld"
ciphertext = enigma.input_string(plaintext)

print(f"\nPlaintext:  {plaintext}")
print(f"Ciphertext: {ciphertext}")

# Reset rotors to initial position for decryption
rotor1.set_position(0)
rotor2.set_position(0)
rotor3.set_position(0)

# Decrypt the message
decrypted = enigma.input_string(ciphertext)
print(f"Decrypted:  {decrypted}")
