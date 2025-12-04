from rich.console import Console
from rich.text import Text
import copy

# Import from this package
from enigmapython.EnigmaZRotorI import EnigmaZRotorI
from enigmapython.EnigmaZRotorII import EnigmaZRotorII
from enigmapython.EnigmaZRotorIII import EnigmaZRotorIII
from enigmapython.EnigmaZEtw import EnigmaZEtw
from enigmapython.EnigmaZ import EnigmaZ
from enigmapython.ReflectorUKW_EnigmaZ import ReflectorUKW_EnigmaZ
from enigmapython.XRay import XRay
import rich
from enigmapython.EnigmaM4RotorI import EnigmaM4RotorI
from enigmapython.EnigmaM4RotorII import EnigmaM4RotorII
from enigmapython.EnigmaM4RotorIII import EnigmaM4RotorIII
from enigmapython.EnigmaM3RotorIV import EnigmaM3RotorIV
from enigmapython.EnigmaM3RotorV import EnigmaM3RotorV
from enigmapython.EnigmaM3RotorVI import EnigmaM3RotorVI
from enigmapython.EnigmaM4RotorBeta import EnigmaM4RotorBeta
from enigmapython.EnigmaM4RotorGamma import EnigmaM4RotorGamma
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.SwappablePlugboard import SwappablePlugboard
from enigmapython.ReflectorUKWB import ReflectorUKWB
from enigmapython.ReflectorUKWBThin import ReflectorUKWBThin
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaM4 import EnigmaM4
from enigmapython.EnigmaM3RotorI import EnigmaM3RotorI
from enigmapython.EnigmaM3RotorII import EnigmaM3RotorII
from enigmapython.EnigmaM3RotorIII import EnigmaM3RotorIII
from enigmapython.EnigmaM3RotorIV import EnigmaM3RotorIV
from enigmapython.EnigmaM3RotorV import EnigmaM3RotorV
from enigmapython.EnigmaM3RotorVI import EnigmaM3RotorVI
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.ReflectorUKWB import ReflectorUKWB
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaM3 import EnigmaM3
from enigmapython.RotatingReflector import RotatingReflector
import logging
import sys

def render_enigma_diagram(enigma):
    """
    Render the Enigma Z ASCII diagram with a variable number of rotors.
    UKW, ETW and Plugboard are always visible. The rotor numbers start from 0.

    Parameters:
    - enigma (Enigma): The Enigma machine to render (minimum 1).
    """
    console = Console()

    rotor_count = len(enigma.rotors)

    rotor_labels = "       ".join([f"Rotor" for i in range(rotor_count - 1, -1, -1)])
    rotor_numbers = "           ".join([f"{i}" for i in range(rotor_count - 1, -1, -1)])

    rotor_walls_top = "     ".join(["+-----+"] * rotor_count)

    rotors_positions = "          ".join(["{:02}".format(enigma.rotors[i].position) for i in range(rotor_count - 1, -1, -1)])

    rotors_rings = "          ".join(["{:02}".format(enigma.rotors[i].ring) for i in range(rotor_count - 1, -1, -1)])

    rotor_walls = "     ".join(["|     |"] * rotor_count)

    rotor_walls_bottom = "     ".join(["+-----+"] * rotor_count)

    rotor_walls_forward = "     ".join(["|  {}  |".format(enigma.rotors[i].journal[-2]['output_char'] if len(enigma.rotors[i].journal) >= 2 else ' ') for i in range(rotor_count - 1, -1, -1)])

    rotor_walls_backward = "     ".join(["|  {}  |".format(enigma.rotors[i].journal[-1]['output_char'] if len(enigma.rotors[i].journal) >= 2 else ' ') for i in range(rotor_count - 1, -1, -1)])

    rotor_wiring_top = "".join(["|-----|--<--"] * rotor_count)

    rotor_wiring_bottom = "".join(["|-----|-->--"] * rotor_count)

    diagram = f"""
            UKW        {rotor_labels}        ETW      PLUGBOARD
                         {rotor_numbers}      
          +-----+     {rotor_walls_top}     +-----+     +-----+
          |     |     {rotor_walls}     |     |     |     |
          |  +--|--<--{rotor_wiring_top}|-----|--<--|-----|----< {enigma.journal[-1]['input_char'] if len(enigma.journal) >= 1 else ' '} <-- Key
          |  |  {rotor_walls_forward}     |  {enigma.etw.journal[-2]['output_char'] if len(enigma.etw.journal) >= 2 else ' '}  |     |  {enigma.plugboard.journal[-2]['output_char'] if len(enigma.plugboard.journal) >= 2 else ' '}  |     |
          |  |  |     {rotor_walls}     |     |     |     |
          |  |  |     {rotor_walls}     |     |     |     |
          |  |  |  {enigma.reflector.journal[-1]['output_char'] if len(enigma.reflector.journal) >= 1 else ' '}  |     {rotor_walls_backward}     |  {enigma.etw.journal[-1]['output_char'] if len(enigma.etw.journal) >= 2 else ' '}  |     |     
          |  +--|-->--{rotor_wiring_bottom}|-----|-->--|-----|----> {enigma.journal[-1]['output_char'] if len(enigma.journal) >= 1 else ' '} --> Lamp
          |     |     {rotor_walls}     |     |     |     |
          +-----+     {rotor_walls_bottom}     +-----+     +-----+

    Pos.:    {"{:02}".format(enigma.reflector.position) if isinstance(enigma.reflector, RotatingReflector) else '  '}          {rotors_positions}    
    Ring:                {rotors_rings}
    """
    console.print(Text(diagram, style="bold"))



rotor1 = EnigmaZRotorI(ring=0,position=0)
rotor2 = EnigmaZRotorI(ring=0,position=0)
rotor3 = EnigmaZRotorI(ring=0,position=0)
reflector = ReflectorUKW_EnigmaZ()
etw = EnigmaZEtw()
enigma = EnigmaZ(rotor3, rotor2, rotor1, reflector, etw, True)
enigma.input_string('0'*41)
print(enigma.reflector)
XRay.render_enigma_xray(enigma)
#render_enigma_diagram(enigma)

plugboard = PlugboardPassthrough()
plugboard = SwappablePlugboard()
plugboard.swap('d', 'c')
rotor1 = EnigmaM4RotorI(0)
rotor2 = EnigmaM4RotorII(0)
rotor3 = EnigmaM4RotorIII(0)
rotor4 = EnigmaM4RotorBeta(0)
reflector = ReflectorUKWBThin()
etw = EtwPassthrough()
enigma = EnigmaM4(plugboard, rotor1, rotor2, rotor3, rotor4, reflector, etw, True)
#print(enigma.input_string('d'))
print(enigma.reflector)
XRay.render_enigma_xray(enigma)
#render_enigma_diagram(enigma)

# Setup logging
#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

plugboard = SwappablePlugboard()
plugboard.swap('m', 'n')
rotor1 = EnigmaM3RotorI(0)
rotor2 = EnigmaM3RotorI(0)
rotor3 = EnigmaM3RotorI(0)
reflector = ReflectorUKWB()
etw = EtwPassthrough()
enigma = EnigmaM3(plugboard,rotor3, rotor2, rotor1,reflector,etw,True)
other_enigma = copy.deepcopy(enigma)
enigma.input_string('d')
print(enigma.reflector)
XRay.render_enigma_xray(enigma)
#render_enigma_diagram(enigma)
#render_enigma_diagram(other_enigma)
XRay.render_enigma_xray(enigma)

#Utils.render_enigma_diagram(other_enigma)