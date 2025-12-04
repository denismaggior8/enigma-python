from enigmapython.EnigmaKRotorI import EnigmaKRotorI
from enigmapython.EnigmaKRotorII import EnigmaKRotorII
from enigmapython.EnigmaKRotorIII import EnigmaKRotorIII
from enigmapython.EnigmaKReflectorUKW import EnigmaKReflectorUKW
from enigmapython.EnigmaKEtw_QWERTZ import EnigmaKEtw_QWERTZ
from enigmapython.EnigmaK import EnigmaK

# Setup Rotors (position, ring)
rotor1 = EnigmaKRotorI(0, 0)      # Right rotor
rotor2 = EnigmaKRotorII(0, 0)     # Middle rotor
rotor3 = EnigmaKRotorIII(0, 0)    # Left rotor

# Setup Reflector
reflector = EnigmaKReflectorUKW()

# Setup ETW (QWERTZ layout)
etw = EnigmaKEtw_QWERTZ()

# Create Enigma K machine (Commercial Enigma - no plugboard)
enigma = EnigmaK(rotor1, rotor2, rotor3, reflector, etw, True)

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
