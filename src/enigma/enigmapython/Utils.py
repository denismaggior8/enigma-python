from importlib import import_module
from rich.console import Console
from rich.text import Text
from enigmapython.RotatingReflector import RotatingReflector


class Utils:

    @staticmethod
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
        return Text(diagram, style="bold")

    @staticmethod
    def find_divergence(str1, str2):
        """
        Finds the index where two strings first diverge, 
        and the characters at that index in both strings.
        
        Parameters:
        str1 (str): The first string.
        str2 (str): The second string.
        
        Returns:
        tuple: (index, char1, char2) where index is the position of divergence,
            char1 is the character in str1 at the divergence,
            and char2 is the character in str2 at the divergence.
            If the strings only diverge in length, char1 and char2 will be None.
            If the strings are identical, returns None.
        """
        # Iterate through both strings up to the length of the shorter string
        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                return i, str1[i], str2[i]  # Return the index and differing characters
        
        # If the strings differ in length
        if len(str1) != len(str2):
            return min(len(str1), len(str2)), None, None
        
        # If the strings are identical
        return None

    @staticmethod
    def find_all_subclasses(cls):
        return set(cls.__subclasses__()).union(
            [s for c in cls.__subclasses__() for s in Utils.find_all_subclasses(c)])

    @staticmethod
    def get_class_instance(cls):
        try:
            module_path, class_name = cls.rsplit('.', 1)
            module = import_module(module_path)
            return getattr(module, class_name)
        except (ImportError, AttributeError) as e:
            raise ImportError(cls)

    @staticmethod    
    def swap_chars(string, ch1, ch2):
        if ch1 == ch2: return string
        str_list = []
        for char in string:
            if char == ch1:
                str_list.append(ch2)
            elif char == ch2:
                str_list.append(ch1)
            else:
                str_list.append(char)
        return ''.join(str_list)
    