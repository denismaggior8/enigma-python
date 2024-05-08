# Enigma Python library

![](img/logo.jpg)

## About

Welcome to **enigmapython**, a Python package designed to emulate the legendary Enigma cryptographic machine used during World War II. **enigmapython** provides a faithful implementation of the Enigma machine, allowing users to explore and understand the workings of this historic device.

## Key Features

- **Flexible Configuration**: **enigmapython** allows customization of the Enigma machine configuration, enabling users to experiment with different rotor settings, reflectors, and ring positions.
- **Easy Extension**: **enigmapython** is designed to be easily extensible, allowing developers to add new features or enhance the existing implementation.
- **Simple yet faithful**: don't be fooled by its simplicity; **enigmapython** implements 100% the algorithms of many Enigma machine models, allowing to decode a message that has been encoded by a real Enigma machine and also the contrary.

## Machines implementations

The following Enigma machine models (along with their rotors, reflectors and plugboards) have been implemented:

### Enigma I 

| Scrambler 	             | Wiring                    	        | Notch 	| Implemented 	    |
|-------	                 |----------------------------	        |-------	|-------------      |
| Plugboard (passthrough+swappable)    | N/A 	        | N/A     	|   ✅           	|
| ETW       (passthrough)    | abcdefghijklmnopqrstuvwxyz 	        | N/A     	|   ✅           	|
| Rotor I                    | ekmflgdqvzntowyhxuspaibrcj 	        | q     	|   ✅           	|
| Rotor II                   | ajdksiruxblhwtmcqgznpyfvoe 	        | e     	|   ✅           	|
| Rotor III                  | bdfhjlcprtxvznyeiwgakmusqo 	        | v     	|   ✅           	|
| Reflector A                | ejmzalyxvbwfcrquontspikhgd 	        | N/A     	|   ✅           	|
| Reflector B                | yruhqsldpxngokmiebfzcwvjat 	        | N/A     	|   ✅           	|
| Reflector C                | fvpjiaoyedrzxwgctkuqsbnmhl 	        | N/A     	|   ✅           	|

### Enigma I Norway (Norenigma)

| Scrambler 	             | Wiring                    	        | Notch 	| Implemented 	    |
|-------	                 |----------------------------	        |-------	|-------------      |
| Plugboard (passthrough+swappable)    | N/A 	        | N/A     	|   ✅           	|
| ETW       (passthrough)    | abcdefghijklmnopqrstuvwxyz 	        | N/A     	|   ✅           	|
| Rotor I                    | wtokasuyvrbxjhqcpzefmdinlg 	        | q     	|   ✅           	|
| Rotor II                   | gjlpubswemctqvhxaofzdrkyni 	        | e     	|   ✅           	|
| Rotor III                  | jwfmhnbpusdytixvzgrqlaoekc 	        | v     	|   ✅           	|
| Rotor IV                   | fgzjmvxepbwshqtliudykcnrao 	        | j     	|   ✅           	|
| Rotor V                    | hejxqotzbvfdascilwpgynmurk 	        | z     	|   ✅           	|
| Reflector UKW              | mowjypuxndsraibfvlkzgqchet 	        | N/A     	|   ✅           	|

### Enigma I Sondermaschine (special machine)

| Scrambler 	             | Wiring                    	        | Notch 	| Implemented 	    |
|-------	                 |----------------------------	        |-------	|-------------      |
| Plugboard (passthrough+swappable)    | N/A 	        | N/A     	|   ✅           	|
| ETW       (passthrough)    | abcdefghijklmnopqrstuvwxyz 	        | N/A     	|   ✅           	|
| Rotor I                    | veosirzujdqckgwypnxaflthmb 	        | q     	|   ✅           	|
| Rotor II                   | uemoatqlshpkcyfwjzbgvxidnr 	        | e     	|   ✅           	|
| Rotor III                  | tzhxmbsipnurjfdkeqvcwglaoy 	        | v     	|   ✅           	|
| Reflector UKW              | ciagsndrbytpzfulvhekoqxwjm 	        | N/A     	|   ✅           	|


### Enigma M3

| Scrambler 	             | Wiring                    	        | Notch 	| Implemented 	    |
|-------	                 |----------------------------	        |-------	|-------------      |
| Plugboard (passthrough+swappable)    | N/A 	        | N/A     	|   ✅           	|
| ETW       (passthrough)    | abcdefghijklmnopqrstuvwxyz 	        | N/A     	|   ✅           	|
| Rotor I                    | ekmflgdqvzntowyhxuspaibrcj 	        | q     	|   ✅           	|
| Rotor II                   | ajdksiruxblhwtmcqgznpyfvoe 	        | e     	|   ✅           	|
| Rotor III                  | bdfhjlcprtxvznyeiwgakmusqo 	        | v     	|   ✅           	|
| Rotor IV                   | esovpzjayquirhxlnftgkdcmwb 	        | j     	|   ✅           	|
| Rotor V                    | vzbrgityupsdnhlxawmjqofeck 	        | z     	|   ✅           	|
| Rotor VI                   | jpgvoumfyqbenhzrdkasxlictw 	        | m, z     	|   ✅           	|
| Rotor VII                  | nzjhgrcxmyswboufaivlpekqdt 	        | m, z     	|   ✅           	|
| Rotor VIII                 | fkqhtlxocbjspdzramewniuygv 	        | m, z     	|   ✅           	|
| Reflector B                | yruhqsldpxngokmiebfzcwvjat 	        | N/A     	|   ✅           	|
| Reflector C                | fvpjiaoyedrzxwgctkuqsbnmhl 	        | N/A     	|   ✅           	|

### Enigma M4

| Scrambler 	             | Wiring                    	        | Notch 	| Implemented 	    |
|-------	                 |----------------------------	        |-------	|-------------      |
| Plugboard (passthrough+swappable)    | N/A 	        | N/A     	|   ✅           	|
| ETW       (passthrough)    | abcdefghijklmnopqrstuvwxyz 	        | N/A     	|   ✅           	|
| Rotor I                    | ekmflgdqvzntowyhxuspaibrcj 	        | q     	|   ✅           	|
| Rotor II                   | ajdksiruxblhwtmcqgznpyfvoe 	        | e     	|   ✅           	|
| Rotor III                  | bdfhjlcprtxvznyeiwgakmusqo 	        | v     	|   ✅           	|
| Rotor IV                   | esovpzjayquirhxlnftgkdcmwb 	        | j     	|   ✅           	|
| Rotor V                    | vzbrgityupsdnhlxawmjqofeck 	        | z     	|   ✅           	|
| Rotor VI                   | jpgvoumfyqbenhzrdkasxlictw 	        | m, z     	|   ✅           	|
| Rotor VII                  | nzjhgrcxmyswboufaivlpekqdt 	        | m, z     	|   ✅           	|
| Rotor VIII                 | fkqhtlxocbjspdzramewniuygv 	        | m, z     	|   ✅           	|
| Beta                       | leyjvcnixwpbqmdrtakzgfuhos 	        | N/A      	|   ✅           	|
| Gamma                      | fsokanuerhmbtiycwlqpzxvgjd 	        | N/A      	|   ✅           	|
| Reflector B Thin           | enkqauywjicopblmdxzvfthrgs 	        | N/A     	|   ✅           	|
| Reflector C Thin           | rdobjntkvehmlfcwzaxgyipsuq 	        | N/A     	|   ✅           	|

## Prerequisites

- Python 3.11
- Clone this repo, checkout the desired branch/tag and install requirements (`pip install -r requirements.txt`) or directly from PyPI using `pip install enigmapython`

## Getting started

Please have a look of the [examples](https://github.com/denismaggior8/enigma-python/blob/master/examples/enigma_machines_examples.py) folder

## Documentation

An initial documentation draft can be found [here](./docs/README.md), but in most cases examples, code (and comments) are better than the documentation

## Credits/references

- Early days experiments with Python and Enigma (where this repo comes from) can be found at: https://github.com/denismaggior8/enigma-cypher
- Rotors wirings have been taken from Crypto Museum at this link  https://www.cryptomuseum.com/crypto/enigma/wiring.htm
- Thanks to 
    - Piotte13 https://piotte13.github.io/enigma-cipher/
    - Cryptii https://cryptii.com
    - PyEnigma https://pypi.org/project/pyenigma/
    - 101 computing https://www.101computing.net/enigma-machine-emulator/ 
    
    for having helped me testing the correctness of the generated ciphertexts 


