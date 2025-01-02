from rich.console import Console
from rich.text import Text

# Import from this package
from enigmapython.EnigmaZRotorI import EnigmaZRotorI
from enigmapython.EnigmaZRotorII import EnigmaZRotorII
from enigmapython.EnigmaZRotorIII import EnigmaZRotorIII
from enigmapython.EnigmaZEtw import EnigmaZEtw
from enigmapython.EnigmaZ import EnigmaZ
from enigmapython.ReflectorZUKW import ReflectorZUKW
from enigmapython.Utils import Utils
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
import logging
import sys

def render_enigma_diagram(enigma):
    """
    Render the Enigma Z ASCII diagram with a variable number of rotors.
    UKW and the first rotor are always visible. The rotor numbers start from 0.

    Parameters:
    - rotor_count (int): Number of rotors to display (minimum 1).
    """
    console = Console()

    rotor_count = len(enigma.rotors)
    # Assicurarsi che ci sia almeno 1 rotore
    if rotor_count < 1:
        rotor_count = 1

    # Etichette per i rotori (dove i numeri dei rotori partono da 0)
    rotor_labels = "       ".join([f"Rotor" for i in range(rotor_count - 1, -1, -1)])
    rotor_numbers = "           ".join([f"{i}" for i in range(rotor_count - 1, -1, -1)])

    # Diagramma dei rotori (dove "___" è la parte superiore di ogni rotore)
    rotor_walls_top = "     ".join(["+-----+"] * rotor_count)

    # Diagramma dei rotori (dove "___" è la parte superiore di ogni rotore)
    rotors_positions = "          ".join(["{:02}".format(enigma.rotors[i].position) for i in range(rotor_count - 1, -1, -1)])

    # Diagramma dei rotori (dove "___" è la parte superiore di ogni rotore)
    rotors_rings = "          ".join(["{:02}".format(enigma.rotors[i].ring) for i in range(rotor_count - 1, -1, -1)])


    # Linea verticale per ogni rotore
    rotor_walls = "     ".join(["|     |"] * rotor_count)

    # Linea verticale per ogni rotore
    rotor_walls_bottom = "     ".join(["+-----+"] * rotor_count)

    # Linea verticale per ogni rotore
    rotor_walls_forward = "     ".join(["|  {}  |".format(enigma.rotors[i].journal[0]['output_char']) for i in range(rotor_count - 1, -1, -1)])

    rotor_walls_backward = "     ".join(["|  {}  |".format(enigma.rotors[i].journal[1]['output_char']) for i in range(rotor_count - 1, -1, -1)])

    # Linea cablaggio per ogni rotore
    rotor_wiring_top = "".join(["|-----|--<--"] * rotor_count)

    rotor_wiring_bottom = "".join(["|-----|-->--"] * rotor_count)

    # Crea il diagramma con le parti dinamiche
    diagram = f"""
            UKW        {rotor_labels}        ETW      PLUGBOARD
                         {rotor_numbers}      
          +-----+     {rotor_walls_top}     +-----+     +-----+
          |     |     {rotor_walls}     |     |     |     |
          |  +--|--<--{rotor_wiring_top}|-----|--<--|-----|----< {enigma.last_input_char} <-- Key
          |  |  {rotor_walls_forward}     |  {enigma.etw.journal[0]['output_char']}  |     |  {enigma.plugboard.journal[0]['output_char']}  |     |
          |  |  |     {rotor_walls}     |     |     |     |
          |  |  |     {rotor_walls}     |     |     |     |
          |  |  |  {enigma.reflector.journal[0]['output_char']}  |     {rotor_walls_backward}     |  {enigma.etw.journal[1]['output_char']}  |     |     
          |  +--|-->--{rotor_wiring_bottom}|-----|-->--|-----|----> {enigma.plugboard.journal[1]['output_char']} --> Lamp
          |     |     {rotor_walls}     |     |     |     |
          +-----+     {rotor_walls_bottom}     +-----+     +-----+

    Pos.:                {rotors_positions}    
    Ring:                {rotors_rings}
    """

    # Stampa il diagramma con rich
    console.print(Text(diagram, style="bold"))

# Esempio con numero variabile di rotori (sempre almeno 1)
rotor_count = 5  # Modifica questo valore per cambiare il numero di rotori


#rotor1 = EnigmaZRotorI(ring=0,position=0)
#rotor2 = EnigmaZRotorI(ring=0,position=0)
#rotor3 = EnigmaZRotorI(ring=0,position=0)
#reflector = ReflectorZUKW()
#etw = EnigmaZEtw()
#enigma = EnigmaZ(rotor3, rotor2, rotor1, reflector, etw, True)
#enigma.input_string('0'*40)
#render_enigma_diagram(enigma)

#plugboard = PlugboardPassthrough()
#rotor1 = EnigmaM4RotorI(0)
#rotor2 = EnigmaM4RotorII(0)
#rotor3 = EnigmaM4RotorIII(0)
#rotor4 = EnigmaM4RotorBeta(0)
#reflector = ReflectorUKWB()
#etw = EtwPassthrough()
#enigma = EnigmaM4(plugboard, rotor1, rotor2, rotor3, rotor4, reflector, etw, True)
#enigma.input_string('d')
#render_enigma_diagram(enigma)

# Setup logging
#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

plugboard = PlugboardPassthrough()
rotor1 = EnigmaM3RotorI(0)
rotor2 = EnigmaM3RotorI(0)
rotor3 = EnigmaM3RotorI(0)
reflector = ReflectorUKWB()
etw = EtwPassthrough()
enigma = EnigmaM3(plugboard,rotor3, rotor2, rotor1,reflector,etw,True)
enigma.input_string('d')
print(enigma.rotors[0].journal)
render_enigma_diagram(enigma)

#Utils.render_enigma_diagram(enigma)