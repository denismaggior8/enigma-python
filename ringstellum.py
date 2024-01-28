def get_index(letter, alphabet):
        '''Get index of letter in alphabet'''
        for i in range(0, len(alphabet)):
            if alphabet[i] == letter:
                return i
 
 
def shift(letter, shift, alphabet):
        '''Shift letter up/down in the alphabet by given shift'''
        for i in range(0, len(alphabet)):
            if alphabet[i] == letter:
                return alphabet[(i + shift) % len(alphabet)]
 
 
import sys
 
print("################################################\n\n")
# Alphabet variable
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Set ringstellung
ringstellung = get_index(sys.argv[1].upper(), alphabet)
print("Ringstellung: " + str(ringstellung))
# Set wiring variable
wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
# Set dot position to postion of A in current wiring
dot_position = get_index("A", wiring)
print("Dot position: " + str(dot_position))
# Loop over all letters before ringstellung (in the alpabet); e.g.: ringstellung 5: loop: 0, 1, 2, 3, 4 
for i in range(0, ringstellung):
    # Set temporary wiring variable
    temp_wiring = wiring
    # Set acutall wiring to empty string
    wiring = ""
    # Loop over chars in temporary wiring
    for char in temp_wiring:
        # Shift the char by one and add that shiftet char to wiring variable
        wiring += shift(char, 1, alphabet)
    # Add one to dot position, make sure we don't exceed the lenght of the alphabet
    dot_position = (dot_position + 1) % len(alphabet)
    print("Wiring shiftet up the alphabet: " + wiring)
    print("New dot position: " + str(dot_position))
i = 0;
# While the letter at the dot position doesn't match with the ringstellung
while not wiring[dot_position] == alphabet[ringstellung]:
    i += 1;
    # Rotate the wiring
    wiring = wiring[-1:] + wiring[:-1]
    print("Rotation " + str(i).zfill(2) + "; Wiring: " + wiring)
 
print("--------------------------------------")
print("Ringstellung: " + alphabet[ringstellung])
print("Final mapping:")
print(alphabet)
print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
print(wiring)
print("--------------------------------------")
print("################################################\n\n")