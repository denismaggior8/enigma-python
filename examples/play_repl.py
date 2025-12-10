import sys
import time
import random
import io
import contextlib

# Add src/enigma to path so imports work
import os
sys.path.append(os.path.join(os.getcwd(), "src", "enigma"))

# Silent imports and setup
silent_setup = [
    "from enigmapython.EnigmaM4RotorI import EnigmaM4RotorI",
    "from enigmapython.EnigmaM4RotorII import EnigmaM4RotorII",
    "from enigmapython.EnigmaM4RotorIII import EnigmaM4RotorIII",
    "from enigmapython.EnigmaM4RotorBeta import EnigmaM4RotorBeta",
    "from enigmapython.ReflectorUKWBThin import ReflectorUKWBThin",
    "from enigmapython.SwappablePlugboard import SwappablePlugboard",
    "from enigmapython.EtwPassthrough import EtwPassthrough",
    "from enigmapython.EnigmaM4 import EnigmaM4",
    "import logging",
    "import sys",
    "logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, force=True)",
]

# Visible commands
commands = [
    "plugboard = SwappablePlugboard()",
    'plugboard.bulk_swap({"a":"c","d":"z"})',
    "rotor1 = EnigmaM4RotorI(0)",
    "rotor2 = EnigmaM4RotorII(0)",
    "rotor3 = EnigmaM4RotorIII(0)",
    "rotor4 = EnigmaM4RotorBeta(0)",
    "reflector = ReflectorUKWBThin()",
    "etw = EtwPassthrough()",
    "enigma = EnigmaM4(plugboard, rotor1, rotor2, rotor3, rotor4, reflector, etw, True)",
    'print(enigma.input_char("c"))',
    'print(enigma.input_char("i"))',
    'print(enigma.input_char("a"))',
    'print(enigma.input_char("o"))',
    'print(enigma.input_string("supercalifragilistichespiralidoso"))'
]

env = {}

def type_str(s):
    sys.stdout.write(">>> ")
    sys.stdout.flush()
    time.sleep(0.2)
    for char in s:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(0.01, 0.08)) # Simulate typing
    sys.stdout.write("\n")
    sys.stdout.flush()
    time.sleep(0.3)

print("Python 3.14.0 (main, Dec 10 2025, 12:00:00) [Clang 16.0.0 (clang-1600.0.26.4)] on darwin")
print('Type "help", "copyright", "credits" or "license" for more information.')

# Execute silent setup
for cmd in silent_setup:
    exec(cmd, env)

# Show comment about omitted details
sys.stdout.write(">>> # Imports and logging configuration have been omitted for brevity\n")
sys.stdout.flush()
time.sleep(0.5)

for cmd in commands:
    type_str(cmd)
    
    # Capture stdout/stderr
    f = io.StringIO()
    try:
        with contextlib.redirect_stdout(f), contextlib.redirect_stderr(f):
             exec(cmd, env)
    except Exception as e:
        # If exec fails, we definitely want to see it
        sys.stdout.write(f"Traceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n{e}\n")
    
    output = f.getvalue()
    if output:
        # In a real REPL, output doesn't have a prefix, but logging does
        sys.stdout.write(output)
        sys.stdout.flush()
        
    time.sleep(0.2)
