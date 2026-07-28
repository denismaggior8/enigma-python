# Enigma Python - Developer & Agent Guide

Welcome, future Agent! This document contains all the critical architectural, mechanical, and development information about the `enigmapython` project. Read it carefully before proposing any modifications or writing new code.

---

## 1. Project Overview & Context
`enigmapython` is a Python library that emulates historical Enigma cryptographic machines with 100% accuracy.
- **Historical Accuracy**: Verified against authentic German Army messages from 1930 and U-boat U-534 messages (M4 model).
- **Extensibility**: Designed to allow custom machines with custom rotors, reflectors, and plugboard configurations.
- **MicroPython Support**: The codebase maintains strict compatibility with MicroPython to support microcontrollers and embedded devices via the [micropython-enigma-python](https://github.com/denismaggior8/micropython-enigma-python) side-project.

---

## 2. Codebase Structure & Key Files
The primary implementation resides inside `src/enigma/enigmapython/`. Here are the core files:

### Core Components
- **[Enigma.py](src/enigma/enigmapython/Enigma.py)**: The main orchestrator. It manages the flow of scrambling signals: ETW -> Plugboard -> Rotors (Right to Left) -> Reflector -> Rotors (Left to Right) -> ETW -> Plugboard.
- **[Rotor.py](src/enigma/enigmapython/Rotor.py)**: Represents an Enigma rotor (scrambler), managing its wiring, turnover position, position, and ring settings.
- **[DynamicTurnoverRotor.py](src/enigma/enigmapython/DynamicTurnoverRotor.py)**: Extends standard `Rotor` to allow dynamic turnover calculation (e.g., commercial Enigma D models).
- **[Reflector.py](src/enigma/enigmapython/Reflector.py)** & **[SettableReflector.py](src/enigma/enigmapython/SettableReflector.py)**: Represent reflectors. Settable reflectors (like those in M4) have rings and positions.
- **[Plugboard.py](src/enigma/enigmapython/Plugboard.py)** & **[SwappablePlugboard.py](src/enigma/enigmapython/SwappablePlugboard.py)**: Manage letter-pair swapping on the plugboard.
- **[Etw.py](src/enigma/enigmapython/Etw.py)**: Entry Wheel (ETW) routing logic.
- **[Alphabets.py](src/enigma/enigmapython/Alphabets.py)**: Contains standard alphabets used by the machines (e.g., lowercase 26-char latin, numeric Z30 alphabet).
- **[XRay.py](src/enigma/enigmapython/XRay.py)**: A diagnostic visualization tool to trace and render signal path stepping details in a human-readable TUI format.

### Historical Models
Individual historically-accurate models are pre-packaged:
- **Enigma I / M3 / M4**: The military models (Wehrmacht / Kriegsmarine).
- **Enigma B / D / K / Swiss K / Z**: Commercial and specialized models.
These models reside in individual files inside `src/enigma/enigmapython/` (e.g., [EnigmaI.py](src/enigma/enigmapython/EnigmaI.py), [EnigmaM4.py](src/enigma/enigmapython/EnigmaM4.py)).

---

## 3. Core Mechanics & Mathematical Concepts

### Rotor Ordering & Signal Path
- **Order**: In the `Enigma` class constructor, `rotors` are passed as a list ordered from **Right to Left** (Fastest to Slowest).
  - `self.rotors[0]` is the Rightmost (Fast/Entry) rotor.
  - `self.rotors[len(self.rotors)-1]` is the Leftmost (Slow) rotor.
- **Signal Flow**:
  1. Plugboard swaps input character (if applicable).
  2. ETW maps the signal into the scrambler.
  3. Signal passes through each rotor right-to-left: from `rotor[0]` up to `rotor[n]`.
  4. Reflector reverses the signal.
  5. Signal passes back through each rotor left-to-right: from `rotor[n]` down to `rotor[0]`.
  6. ETW maps signal backwards.
  7. Plugboard swaps output character (if applicable).

### Stepping & Observer Pattern
Rotor stepping is modeled using an Observer Pattern (defined in [Observer.py](src/enigma/enigmapython/Observer.py) and [Observable.py](src/enigma/enigmapython/Observable.py)):
- Rotors notify their parent `Enigma` machine observer when they step **away** from their turnover position.
- Specifically, the check in `Rotor.increment_position()` triggers notification if `self.position == (turnover_index + 1) % len(alphabet)`.
- When notified, the `Enigma` observer increments the next rotor to the left.

### The Double-Step Anomaly
To simulate the mechanical double-stepping behavior of real Enigma machines:
- If a rotor (except the leftmost) is moved *onto* its turnover position, its `double_step_triggered` flag is set to `True`.
- On the next keypress (before processing the character), the machine sweeps all rotors. If `double_step_triggered` is `True`, the rotor increments its position once more, and clears the flag.
- This creates the classic mechanical "kick" behavior, where the middle rotor steps on consecutive letters.
- See detailed mechanics documentation in [mechanics.md](docs/mechanics.md).

### Ring Settings (Ringstellung) vs. Positions (Grundstellung)
- **Position (`position`)**: The current rotation of the rotor as shown on the dials.
- **Ring (`ring`)**: The offset between the internal wiring core and the alphabet ring. Modifying the ring setting shifts the virtual turnover position and the wiring permutation indices.
- Inherited from the abstract class **[Settable.py](src/enigma/enigmapython/Settable.py)**.

---

## 4. Development & MicroPython Guidelines
This codebase is strictly kept compatible with standard CPython 3.11 AND MicroPython.

> [!IMPORTANT]
> **Maintain MicroPython Compatibility:**
> 1. Avoid advanced Python Standard Library modules (e.g., `inspect`, complex `typing`, complex regex/multiprocessing) that are missing or restricted on MicroPython.
> 2. Use standard loops and list comprehensions. Keep object allocations to a minimum inside critical path methods like `input_char` or `process_char`.
> 3. **Rotor / Instance Comparisons**: Use the `is` operator to compare rotor instances in callbacks (e.g., `rotor is observable`). Do not override `__eq__` in a way that breaks instance identity checks, as MicroPython list lookups rely heavily on this.
> 4. Keep files and classes clean and modular.

---

## 5. Testing & Verification

### Executing Tests
Tests are configured using **pytest** (configured in [pytest.ini](pytest.ini)). To run all tests:
```bash
python3 -m pytest
```

### Verification & Validation Strategy
- Tests inside the `tests/` directory (e.g., [Enigma1930_tests.py](tests/Enigma1930_tests.py), [EnigmaM4_U534_tests.py](tests/EnigmaM4_U534_tests.py)) check correct decryption of historical keys and transcripts.
- Integration tests (like [EnigmaM4_tests.py](tests/EnigmaM4_tests.py)) validate output against the widely-accepted third-party package `py-enigma` using long random strings (up to 1,000,000 characters) to guarantee absolute cryptographic alignment.
