"""
Enigma M4 Mini Brute-Forcer Example

This script demonstrates how cryptanalysts brute-forced Enigma messages. 
We simulate a scenario where we have intercepted a ciphertext and have a "crib"
(a known piece of plaintext, like 'wettervorhersage'). 

We know the machine setup (rotors used, reflectors, plugboard), but we DO NOT 
know the initial 3 rotor positions. Python will simulate all 17,576 possible 
starting positions to find the key.
"""

import time
import logging
from enigmapython.EnigmaM4RotorI import EnigmaM4RotorI
from enigmapython.EnigmaM4RotorII import EnigmaM4RotorII
from enigmapython.EnigmaM4RotorIII import EnigmaM4RotorIII
from enigmapython.EnigmaM4RotorBeta import EnigmaM4RotorBeta
from enigmapython.ReflectorUKWBThin import ReflectorUKWBThin
from enigmapython.SwappablePlugboard import SwappablePlugboard
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaM4 import EnigmaM4

def main():
    # Setup logging to be quiet for brute-forcing
    logging.getLogger().setLevel(logging.WARNING)
    
    # ----------------------------------------------------
    # 1. ENCRYPTING A MESSAGE WITH SECRET ROTOR POSITIONS
    # ----------------------------------------------------
    print("--- 1. ENCRYPTING MESSAGE WITH SECRET POSITIONS ---")
    
    # These are our "secret" starting positions: P, Y, T, H
    # We use numeric indices (0-25).
    # rotor1 = Fast Rotor (Right), rotor2 = Middle, rotor3 = Slow (Left)
    # rotor4 = Greek Rotor (Leftmost, never steps)
    secret_positions = (14, 2, 9, 21) # we assign them to r1, r2, r3, r4
    
    plugboard = SwappablePlugboard()
    
    r1 = EnigmaM4RotorI(secret_positions[0])
    r2 = EnigmaM4RotorII(secret_positions[1])
    r3 = EnigmaM4RotorIII(secret_positions[2])
    r4 = EnigmaM4RotorBeta(secret_positions[3])
    reflector = ReflectorUKWBThin()
    etw = EtwPassthrough()
    
    encrypt_machine = EnigmaM4(plugboard, r1, r2, r3, r4, reflector, etw, True)
    
    # German Enigma operators used X for spaces and punctuation
    plaintext = "wettervorhersagexostseexheutexabendix"
    ciphertext = encrypt_machine.input_string(plaintext)
    
    print(f"Known Plaintext:  {plaintext}")
    print(f"Generated Cipher: {ciphertext}\n")
    
    # ----------------------------------------------------
    # 2. BRUTE FORCING 3 ROTORS (17,576 combinations)
    # ----------------------------------------------------
    # Assume we intercepted 'ciphertext', and we guess the crib "wettervorhersage"
    # We must brute-force the 3 regular rotors.
    crib = "wettervorhersage"
    
    print("--- 2. BRUTE FORCING 3 ROTORS (17,576 possible keys) ---")
    print(f"Looking for crib: '{crib}'")
    print(f"Scanning keyspace. This might take roughly 10-30 seconds...")
    
    start_time = time.time()
    
    # We pre-setup a search machine to avoid re-instantiating objects
    search_r1 = EnigmaM4RotorI(0)
    search_r2 = EnigmaM4RotorII(0)
    search_r3 = EnigmaM4RotorIII(0)
    search_r4 = EnigmaM4RotorBeta(secret_positions[3]) # Greek rotor position is known
    
    search_machine = EnigmaM4(plugboard, search_r1, search_r2, search_r3, search_r4, reflector, etw, True)
    
    found = False
    attempts = 0
    for p3 in range(26):
        for p2 in range(26):
            for p1 in range(26):
                # Apply guessed positions
                search_r1.position = p1
                search_r2.position = p2
                search_r3.position = p3
                
                # Reset double step triggers
                search_r1.double_step_triggered = False
                search_r2.double_step_triggered = False
                search_r3.double_step_triggered = False
                
                # We also need to clear the journal as we do many iterations
                search_machine.clear_journal()
                
                # Attempt to decrypt
                full_decryption = search_machine.input_string(ciphertext)
                attempts += 1
                
                if crib in full_decryption:
                    print(f"\n[+] MATCH FOUND!")
                    print(f"[+] Positions (r1, r2, r3): {p1}, {p2}, {p3}")
                    print(f"[+] Decrypted Text: {full_decryption}")
                    found = True
                    break
            if found: break
        if found: break
        
    end_time = time.time()
    print(f"\nBrute force completed {attempts} checks in {end_time - start_time:.2f} seconds.")

if __name__ == '__main__':
    main()
