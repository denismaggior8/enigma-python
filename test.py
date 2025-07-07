from enigmapython.EnigmaM4RotorI import EnigmaM4RotorI
from enigmapython.EnigmaM4RotorII import EnigmaM4RotorII
from enigmapython.EnigmaM4RotorIII import EnigmaM4RotorIII
from enigmapython.EnigmaM4RotorBeta import EnigmaM4RotorBeta
from enigmapython.EnigmaM4RotorGamma import EnigmaM4RotorGamma
from enigmapython.EnigmaM4 import EnigmaM4
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.ReflectorUKWBThin import ReflectorUKWBThin
from enigmapython.XRay import XRay


plugboard = PlugboardPassthrough()
rotor1 = EnigmaM4RotorI(1)
rotor2 = EnigmaM4RotorII(15)
rotor3 = EnigmaM4RotorIII(26)
rotor4 = EnigmaM4RotorBeta(4)
reflector = ReflectorUKWBThin()
etw = EtwPassthrough()
enigma = EnigmaM4(plugboard, rotor1, rotor2, rotor3, rotor4, reflector, etw, True)
enigma.input_char("c")
XRay.render_enigma_xray(enigma)
enigma.input_char("c")
XRay.render_enigma_xray(enigma)
print("1".upper())
