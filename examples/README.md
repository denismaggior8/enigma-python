# Enigma Python Examples

This directory contains example scripts demonstrating how to configure and use various Enigma machine models with `enigmapython`.

## Available Examples

### Enigma I
- **File**: [enigma_machine_I_example.py](enigma_machine_I_example.py)
- **Description**: Setup and usage of the standard German Army Enigma I (Wehrmacht) with 3 rotors and a plugboard.

### Enigma I Norway (Norenigma)
- **File**: [enigma_machine_I_norway_example.py](enigma_machine_I_norway_example.py)
- **Description**: Setup and usage of the Enigma I Norway, a variant used by the Norwegian Police Security Service.

### Enigma I Sondermaschine
- **File**: [enigma_machine_I_sondermaschine_example.py](enigma_machine_I_sondermaschine_example.py)
- **Description**: Setup and usage of the Enigma I Sondermaschine, a special machine variant.

### Enigma M3
- **File**: [enigma_machine_M3_example.py](enigma_machine_M3_example.py)
- **Description**: Setup and usage of the Enigma M3 (Kriegsmarine) with 3 rotors.

### Enigma M4
- **File**: [enigma_machine_M4_example.py](enigma_machine_M4_example.py)
- **Description**: Setup and usage of the Enigma M4 (Kriegsmarine U-boat) with 4 rotors (including Beta/Gamma) and a thin reflector.

### Enigma K (Commercial Enigma)
- **File**: [enigma_machine_K_example.py](enigma_machine_K_example.py)
- **Description**: Setup and usage of the Enigma K, the original commercial Enigma machine from the 1920s with QWERTZ keyboard layout. Note: This model does not have a plugboard.

### Enigma B (A-133)
- **File**: [enigma_machine_B_example.py](enigma_machine_B_example.py)
- **Description**: Setup and usage of the rare Enigma B (Swedish model A-133). Note: This model does not have a plugboard.

### Enigma D
- **File**: [enigma_machine_D_example.py](enigma_machine_D_example.py)
- **Description**: Setup and usage of the commercial Enigma D.

### Enigma Z
- **File**: [enigma_machine_Z_example.py](enigma_machine_Z_example.py)
- **Description**: Setup and usage of the Enigma Z (Z30), a numerical-only machine.

### Custom Enigma Machine
- **File**: [enigma_machine_custom_example.py](enigma_machine_custom_example.py)
- **Description**: Demonstrates how to build a fully customized Enigma machine from scratch using the library's base classes (`Rotor`, `Reflector`, `Enigma`).

### Enigma K Swiss
- **File**: [enigma_machine_K_Swiss_example.py](enigma_machine_K_Swiss_example.py)
- **Description**: Setup and usage of the Swiss variant of the Commercial Enigma K.

### Enigma T (Tirpitz)
- **File**: [enigma_machine_T_example.py](enigma_machine_T_example.py)
- **Description**: Setup and usage of the Enigma T (Tirpitz), featuring eight specific rotors and settable reflector UKW-T.

### Mini Brute-Forcer
- **File**: [mini_brute_forcer.py](mini_brute_forcer.py)
- **Description**: Simulates wartime cryptanalysis by brute-forcing all 17,576 starting rotor positions to decrypt an intercepted message given a known plaintext "crib".

### Interactive REPL Demo
- **File**: [play_repl.py](play_repl.py)
- **Description**: An automated interactive terminal presentation simulating setup, rotor/plugboard configuration, and encryption in a Python REPL.

### XRay Real-time Visualization
- **File**: [render_enigma.py](render_enigma.py)
- **Description**: Employs the `XRay` diagnostic utility with `rich` console rendering to trace and display the exact character-by-character signal path stepping details in real-time.

## How to Run

You can run any example directly using python:

```bash
python examples/enigma_machine_I_example.py
```
