from rich.console import Console
from rich.text import Text

from enigmapython.SettableReflector import SettableReflector

class XRay():
    @staticmethod
    def render_enigma_xray(enigma):
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

        rotors_positions = "      ".join(["{} ({:02})".format(enigma.alphabet_list[enigma.rotors[i].position].upper(),enigma.rotors[i].position) for i in range(rotor_count - 1, -1, -1)])

        rotors_rings = "      ".join(["{} ({:02})".format(enigma.alphabet_list[enigma.rotors[i].ring].upper(),enigma.rotors[i].ring) for i in range(rotor_count - 1, -1, -1)])

        reflector_ring = ""

        rotor_walls_position = "     ".join(["|  {}  |".format(enigma.alphabet_list[enigma.rotors[i].position].upper()) for i in range(rotor_count - 1, -1, -1)])

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
              |  +--|--<--{rotor_wiring_top}|-----|--<--|-----|----< {enigma.journal[-1]['input_char'] if len(enigma.journal) >= 1 else ' '} <-- Key ⌨️
              |  |  {rotor_walls_forward}     |  {enigma.etw.journal[-2]['output_char'] if len(enigma.etw.journal) >= 2 else ' '}  |     |  {enigma.plugboard.journal[-2]['output_char'] if len(enigma.plugboard.journal) >= 2 else ' '}  |     |
              |  |  |     {rotor_walls}     |     |     |     |
              |  |  |     {rotor_walls}     |     |     |     |
              |  |  |  {enigma.reflector.journal[-1]['output_char'] if len(enigma.reflector.journal) >= 1 else ' '}  |     {rotor_walls_backward}     |  {enigma.etw.journal[-1]['output_char'] if len(enigma.etw.journal) >= 2 else ' '}  |     |     
              |  +--|-->--{rotor_wiring_bottom}|-----|-->--|-----|----> {enigma.journal[-1]['output_char'] if len(enigma.journal) >= 1 else ' '} --> Lamp 💡
              |     |     {rotor_walls}     |     |     |     |
              +-----+     {rotor_walls_bottom}     +-----+     +-----+

    Pos.:      {"{} ({:02})".format(enigma.alphabet_list[enigma.reflector.position].upper(),enigma.reflector.position) if isinstance(enigma.reflector, SettableReflector) else ' N/A  '}      {rotors_positions}    
    Ring:      {"{} ({:02})".format(enigma.alphabet_list[enigma.reflector.ring].upper(),enigma.reflector.ring) if isinstance(enigma.reflector, SettableReflector) else ' N/A  '}      {rotors_rings}
        """
        console.print(Text(diagram, style="bold"))
        return Text(diagram, style="bold")