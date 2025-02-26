# Enigma Python library

<div class="img-container" style="text-align: center;"> 
    <img src="img/logo.jpg" alt="drawing" width="200" />
</div>

## About

Welcome to **enigmapython**, a Python package designed to emulate the legendary Enigma cryptographic machine used during World War II. **enigmapython** provides a faithful implementation of the Enigma machine, allowing users to explore and understand the workings of this historic device.

## Key Features

- **Flexible Configuration**: **enigmapython** allows customization of the Enigma machine configuration, enabling users to experiment with different rotor settings, reflectors, and ring positions.
- **Easy Extension**: **enigmapython** is designed to be easily extensible, allowing developers to add new features or enhance the existing implementation.
- **Simple yet faithful**: don't be fooled by its simplicity; **enigmapython** implements 100% the algorithms of many Enigma machine models, allowing to decode a message that has been encoded by a real Enigma machine and also the contrary.

## Machines implementations

The following Enigma machine models (along with their rotors, reflectors and plugboards) have been implemented:

### Enigma B (Sweden, s/n: A-133)*

| Scrambler 	             | Wiring                    	        | Notch 	| Implemented 	    |
|-------	                 |----------------------------	        |-------	|-------------      |
| ETW       (passthrough)    | abcdefghijklmnopqrstuvxyzåäö 	    | N/A     	|   ✅           	|
| Rotor I                    | psbgöxqjdhoäucfrtezvåinlymka         | ä     	|   ✅           	|
| Rotor II                   | chnsyöadmotrzxbäigåekqupflvj 	    | ä     	|   ✅           	|
| Rotor III                  | åvqiaäxrjbözspcfyunthdomekgl 	    | ä     	|   ✅           	|
| Reflector UKW              | ldgbäncpskjavfzhxuiårmqöotey 	    | N/A     	|   ✅           	|

*given the rarity of this model and the little documentation/simulators available, although I expect an encryption consistency on par with newer models, I was unable to test it as I would have liked

### Enigma D

| Scrambler 	             | Wiring                    	        | Notch 	| Implemented 	    |
|-------	                 |----------------------------	        |-------	|-------------      |
| ETW "QWERTZ"               | qwertzuioasdfghjkpyxcvbnml 	        | N/A     	|   ✅           	|
| ETW "JWULCM"               | jwulcmnohpqzyxiradkegvbtsf 	        | N/A     	|   ✅           	|
| Rotor I                    | lpgszmhaeoqkvxrfybutnicjdw 	        | y     	|   ✅           	|
| Rotor II                   | slvgbtfxjqohewirzyamkpcndu 	        | e     	|   ✅           	|
| Rotor III                  | bdfhjlcprtxvznyeiwgakmusqo 	        | n     	|   ✅           	|
| Reflector UKW              | imetcgfraysqbzxwlhkdvupojn 	        | N/A     	|   ✅           	|


### Enigma Z (Z30 Mark I)*

| Scrambler 	             | Wiring                     | Notch | Implemented |
|-------	                 |----------------------------|-------|-------------|
| ETW       (passthrough)    | 1234567890 	    | N/A     |   ✅  |
| Rotor I                    | 6418270359       | 9       |   ✅  |
| Rotor II                   | 5841097632 	    | 9       |   ✅  |
| Rotor III                  | 3581620794 	    | 9       |   ✅  |
| Reflector UKW              | 5079183642 	    | N/A     |   ✅  |

*given the rarity of this model and the little documentation/simulators available, although I expect an encryption consistency on par with newer models, I was unable to test it as I would have liked

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

## Known implementations

Here's a list containing all the known Enigma simulators that use the **enigmapython** API.

- [Enigma TUI](https://github.com/denismaggior8/enigma-tui). **Enigma TUI** is a **T**erminal **U**ser **I**nterface for Enigma machines, allowing you to simulate different Enigma machine models from the terminal. It employs  **enigmapython** as Enigma engine. 

<div class="img-container" style="text-align: center;"> 
    <img src="img/enigmatui.png" alt="drawing" width="400" align="center"/>
</div>


- [Retrocampus BBS Enigma simulator](https://retrocampus.com/bbs/). When connected to the BBS, type E to access an Enigma M3 cypher machine whose backend is based on **enigmapython**.

<div class="img-container" style="text-align: center;">
    <img src="img/retrocampus_enigma.png" alt="drawing" width="400" align="center"/>
</div>

In the case you leveraged **enigmapython** API in a project, either public or not, drop me an email at __denis.maggiorotto[at]gmail.com__ and I'll be happy to list you here.


## Credits/references

- Early days experiments with Python and Enigma (where this repo comes from) can be found at: https://github.com/denismaggior8/enigma-cypher
- Rotors wirings have been taken from **Crypto Museum** at this link  https://www.cryptomuseum.com/crypto/enigma/wiring.htm
- Thanks to 
    - Piotte13 https://piotte13.github.io/enigma-cipher/
    - Cryptii https://cryptii.com
    - PyEnigma https://pypi.org/project/pyenigma/
    - 101 computing https://www.101computing.net/enigma-machine-emulator/ 
    - DenCode Enigma simulator https://dencode.com/cipher/enigma
    - Enigma simulation in Javascript/HTML by Daniel Palloks https://people.physik.hu-berlin.de/~palloks/js/enigma/index_en.html
    - Enigma B A133 simulation in Javascript/HTML by Daniel Palloks https://people.physik.hu-berlin.de/~palloks/js/enigma/enigma-a133_v261_en.html
    - Enigma Z simulation in Javascript/HTML by Daniel Palloks https://people.physik.hu-berlin.de/~palloks/js/enigma/enigma-z_v262b_en.html

    for having helped me testing the correctness of the generated ciphertexts 

## Support

Found it useful/funny/educational? Please consider to [![Buy Me a Coffee](https://img.shields.io/badge/buy_me_a_coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/denismaggior8)