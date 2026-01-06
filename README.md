# Enigma Python library

<div class="img-container" style="text-align: center;"> 
    <img src="https://raw.githubusercontent.com/denismaggior8/enigma-python/master/img/logo.jpg" alt="drawing" width="200" />
</div>

## About

Welcome to **enigmapython**, a Python package designed to emulate the legendary Enigma cryptographic machine used during World War II. **enigmapython** provides a faithful implementation of the Enigma machine, allowing users to explore and understand the workings of this historic device.

<br>
<div class="img-container" style="text-align: center;">
    <a href="https://asciinema.org/a/761182">
        <img src="https://asciinema.org/a/761182.svg" alt="asciicast"/>
    </a>
</div>
<br>


This project is listed on [Wikipedia](https://en.wikipedia.org/wiki/List_of_Enigma_machine_simulators) as a globally recognized Enigma machine simulator, noted for its historical accuracy.

<div class="img-container" style="text-align: center;"> 
    <a href="https://en.wikipedia.org/wiki/List_of_Enigma_machine_simulators">
        <img src="https://img.shields.io/badge/Wikipedia-List%20of%20Enigma%20machine%20simulators-white?style=for-the-badge&logo=wikipedia&logoColor=black" alt="Wikipedia">
    </a>
    <a href="https://pypi.org/project/enigmapython/">
        <img src="https://img.shields.io/pypi/v/enigmapython?style=for-the-badge&logo=pypi&logoColor=white" alt="PyPI version">
    </a>
    <a href="https://pypi.org/project/enigmapython/">
        <img src="https://img.shields.io/pypi/pyversions/enigmapython?style=for-the-badge&logo=python&logoColor=white" alt="Python versions">
    </a>
    <a href="https://pepy.tech/project/enigmapython">
        <img src="https://img.shields.io/pepy/dt/enigmapython?style=for-the-badge&logo=pypi&logoColor=white" alt="Total Downloads">
    </a>
    <a href="https://github.com/denismaggior8/enigma-python">
        <img src="https://img.shields.io/github/stars/denismaggior8/enigma-python?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Stars">
    </a>
    <a href="https://github.com/denismaggior8/enigma-python">
        <img src="https://img.shields.io/github/languages/code-size/denismaggior8/enigma-python?style=for-the-badge&logo=github&logoColor=white" alt="Code Size">
    </a>
    <a href="https://github.com/denismaggior8/enigma-python/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/denismaggior8/enigma-python?style=for-the-badge&logo=github&logoColor=white" alt="License">
    </a>
</div>

## Key Features

- **Flexible Configuration**: **enigmapython** allows customization of the Enigma machine configuration, enabling users to experiment with different rotor settings, reflectors, and ring positions.
- **Easy Extension**: **enigmapython** is designed to be easily extensible, allowing developers to add new features or enhance the existing implementation.
- **Simple yet faithful**: don't be fooled by its simplicity; **enigmapython** implements 100% the algorithms of many Enigma machine models, allowing to decode a message that has been encoded by a real Enigma machine and also the contrary.
    
## Enigma mechanics

For a detailed description of the rotor movement and stepping logic, including pseudocode, please refer to the [Enigma Mechanics](./docs/mechanics.md) documentation.

## Historical Accuracy & Verification

**enigmapython** is rigorously tested against authentic historical data to ensure maximum accuracy.


- [Authentic German Army Test Message from 1930](https://cryptocellar.org/enigma/e-message-1930.html): Documented by Frode Weierud's CryptoCellar, this test validates that the **Enigma I** implementation correctly handles the complex interaction of rotors, ring settings, and plugboard connections exactly as the original machines did. See the [corresponding unit test](https://github.com/denismaggior8/enigma-python/blob/master/tests/Enigma1930_tests.py) for details.
- [Authentic U-534 M4 Message P1030700](https://enigma.hoerenberg.com/index.php?cat=The%20U534%20messages&page=P1030700): A message from the U-534 submarine (May 1945), validating the **Enigma M4** implementation (including the Greek rotor and thin reflector) against historical intercepts. See the [corresponding unit test](https://github.com/denismaggior8/enigma-python/blob/master/tests/EnigmaM4_U534_tests.py) for details.

## Machines implementations

The following Enigma machine models (along with their rotors, reflectors and plugboards) have been implemented:

### Enigma B (Sweden, s/n: A-133)*

| Scrambler 	             | Wiring                    	        | Turnover 	| Implemented 	    |
|-------	                 |----------------------------	        |-------	|-------------      |
| ETW       (passthrough)    | abcdefghijklmnopqrstuvxyzåäö 	    | N/A     	|   ✅           	|
| Rotor I                    | psbgöxqjdhoäucfrtezvåinlymka         | ä     	|   ✅           	|
| Rotor II                   | chnsyöadmotrzxbäigåekqupflvj 	    | ä     	|   ✅           	|
| Rotor III                  | åvqiaäxrjbözspcfyunthdomekgl 	    | ä     	|   ✅           	|
| Reflector UKW              | ldgbäncpskjavfzhxuiårmqöotey 	    | N/A     	|   ✅           	|

*given the rarity of this model and the little documentation/simulators available, although I expect an encryption consistency on par with newer models, I was unable to test it as I would have liked

### Enigma K (Commercial Enigma)

| Scrambler 	             | Wiring                    	        | Turnover 	| Implemented 	    |
|-------	                 |----------------------------	        |-------	|-------------      |
| ETW "QWERTZ"               | qwertzuioasdfghjkpyxcvbnml 	        | N/A     	|   ✅           	|
| Rotor I                    | lpgszmhaeoqkvxrfybutnicjdw 	        | y     	|   ✅           	|
| Rotor II                   | slvgbtfxjqohewirzyamkpcndu 	        | e     	|   ✅           	|
| Rotor III                  | cjgdpshkturawzxfmynqobvlie 	        | n     	|   ✅           	|
| Reflector UKW              | imetcgfraysqbzxwlhkdvupojn 	        | N/A     	|   ✅           	|

### Enigma D (Commercial Enigma)

| Scrambler 	             | Wiring                    	        | Turnover 	| Implemented 	    |
|-------	                 |----------------------------	        |-------	|-------------      |
| ETW "QWERTZ"               | qwertzuioasdfghjkpyxcvbnml 	        | N/A     	|   ✅           	|
| Rotor I                    | lpgszmhaeoqkvxrfybutnicjdw 	        | z*     	|   ✅           	|
| Rotor II                   | slvgbtfxjqohewirzyamkpcndu 	        | z*    	|   ✅           	|
| Rotor III                  | cjgdpshkturawzxfmynqobvlie 	        | z*     	|   ✅           	|
| Reflector UKW              | imetcgfraysqbzxwlhkdvupojn 	        | N/A     	|   ✅           	|

*Enigma D rotor turnover happens at Z when ringstellung is 0 (A), otherwise turnover position is calculated using the formula `turnover = (ringstellung + 1) % 26`.

### Enigma Z (Z30 Mark I)*

| Scrambler 	             | Wiring                     | Turnover | Implemented |
|-------	                 |----------------------------|-------|-------------|
| ETW       (passthrough)    | 1234567890 	    | N/A     |   ✅  |
| Rotor I                    | 6418270359       | 9       |   ✅  |
| Rotor II                   | 5841097632 	    | 9       |   ✅  |
| Rotor III                  | 3581620794 	    | 9       |   ✅  |
| Reflector UKW              | 5079183642 	    | N/A     |   ✅  |

*given the rarity of this model and the little documentation/simulators available, although I expect an encryption consistency on par with newer models, I was unable to test it as I would have liked

### Enigma I 

| Scrambler 	             | Wiring                    	        | Turnover 	| Implemented 	    |
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

| Scrambler 	             | Wiring                    	        | Turnover 	| Implemented 	    |
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

| Scrambler 	             | Wiring                    	        | Turnover 	| Implemented 	    |
|-------	                 |----------------------------	        |-------	|-------------      |
| Plugboard (passthrough+swappable)    | N/A 	        | N/A     	|   ✅           	|
| ETW       (passthrough)    | abcdefghijklmnopqrstuvwxyz 	        | N/A     	|   ✅           	|
| Rotor I                    | veosirzujdqckgwypnxaflthmb 	        | q     	|   ✅           	|
| Rotor II                   | uemoatqlshpkcyfwjzbgvxidnr 	        | e     	|   ✅           	|
| Rotor III                  | tzhxmbsipnurjfdkeqvcwglaoy 	        | v     	|   ✅           	|
| Reflector UKW              | ciagsndrbytpzfulvhekoqxwjm 	        | N/A     	|   ✅           	|


### Enigma M3

| Scrambler 	             | Wiring                    	        | Turnover 	| Implemented 	    |
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

| Scrambler 	             | Wiring                    	        | Turnover 	| Implemented 	    |
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

### Custom Machine

### Custom Machine Configuration

| Scrambler 	             | Wiring                    	        | Turnover 	| Implemented 	    |
|-------	                 |----------------------------	        |-------	|-------------      |
| Plugboard (passthrough+swappable)    | N/A 	        | N/A     	|   ✅           	|
| ETW (Entry Wheel)          | Custom 	        | N/A     	|   ✅           	|
| Rotor                      | Custom 	        | Custom     	|   ✅           	|
| Reflector                  | Custom 	        | N/A     	|   ✅           	|


You can create a fully customized Enigma machine by instantiating the base components manually. This allows you to define custom alphabets, wirings, and turnover positions.

```python
from enigmapython.Enigma import Enigma
from enigmapython.Rotor import Rotor
from enigmapython.Reflector import Reflector
from enigmapython.SwappablePlugboard import SwappablePlugboard
from enigmapython.Etw import Etw
from enigmapython.Alphabets import Alphabets

# 1. Define alphabet
alphabet = Alphabets.lookup.get("latin_i18n_26chars_lowercase")

# 2. Create custom rotors
# Parameters: wiring, turnover_indexes, alphabet, initial_position, ring_setting
rotor1 = Rotor("ekmflgdqvzntowyhxuspaibrcj", [16], alphabet, 0, 0) # Turnover at 'q'
rotor2 = Rotor("ajdksiruxblhwtmcqgznpyfvoe", [4], alphabet, 0, 0)  # Turnover at 'e'
rotor3 = Rotor("bdfhjlcprtxvznyeiwgakmusqo", [21], alphabet, 0, 0) # Turnover at 'v'

# 3. Create custom reflector
reflector = Reflector("yruhqsldpxngokmiebfzcwvjat", alphabet)

# 4. Create other components
# Swappable plugboard allows you to connect pairs of letters
plugboard = SwappablePlugboard(alphabet=alphabet)
plugboard.swap("a", "z") # Example: swap 'a' with 'z'

etw = Etw(alphabet, alphabet) # Passthrough ETW using alphabet as wiring

# 5. Assemble the Enigma machine
engine = Enigma(plugboard, [rotor1, rotor2, rotor3], reflector, etw, auto_increment_rotors=True, alphabet=alphabet)

# 6. Encrypt/Decrypt
cipher = engine.input_string("hello")
print(f"Ciphertext: {cipher}") # Outputs: mfnca
```

## Prerequisites

- Python 3.11
- Clone this repo, checkout the desired branch/tag and install requirements (`pip install -r requirements.txt`) or directly from PyPI using `pip install enigmapython`

## Getting started

Get started by installing the package from PyPI (`pip install enigmapython`) and exploring the examples in the [examples](https://github.com/denismaggior8/enigma-python/tree/master/examples) folder.

## Documentation

Full API documentation is available on [ReadTheDocs](https://enigmapython.readthedocs.io/).

For additional details, you can also refer to the [local documentation](./docs/README.md), examples, and code comments.

## Known implementations

Here's a list containing all the known Enigma simulators that use the **enigmapython** API.

- [Enigma TUI](https://github.com/denismaggior8/enigma-tui). **Enigma TUI** is a **T**erminal **U**ser **I**nterface for Enigma machines, allowing you to simulate different Enigma machine models from the terminal. It employs  **enigmapython** as Enigma engine. 

<div class="img-container" style="text-align: center;"> 
    <img src="https://raw.githubusercontent.com/denismaggior8/enigma-python/master/img/enigmatui.png" alt="drawing" width="400" align="center"/>
</div>
<br>
<br>

- [MicroPython Enigma Python](https://github.com/denismaggior8/micropython-enigma-python). **MicroPython Enigma Python** is a side project to bring Enigma Python library also on ambedded devices which runs MicroPython. It has been referenced on https://awesome-micropython.com/#historical, a curated list of the best MicroPython libraries, in the Cryptography/Historical section.

<div class="img-container" style="text-align: center;"> 
    <img src="https://raw.githubusercontent.com/denismaggior8/enigma-python/master/img/micropython-enigma-python.png" alt="drawing" width="400" align="center"/>
</div>

<br>
<br>

- [Retrocampus BBS Enigma simulator](https://retrocampus.com/bbs/). When connected to the BBS, type E to access an Enigma M3 cypher machine whose backend is based on **enigmapython**.
<div class="img-container" style="text-align: center;">
    <img src="https://raw.githubusercontent.com/denismaggior8/enigma-python/master/img/retrocampus_enigma.png" alt="drawing" width="400" align="center"/>
</div>

<br>
<br>

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
