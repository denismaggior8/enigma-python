# Import from this package
from enigmapython.EnigmaZRotorI import EnigmaZRotorI
from enigmapython.EnigmaZRotorII import EnigmaZRotorII
from enigmapython.EnigmaZRotorIII import EnigmaZRotorIII
from enigmapython.EnigmaZEtw import EnigmaZEtw
from enigmapython.EnigmaZ import EnigmaZ
from enigmapython.ReflectorZUKW import ReflectorZUKW
from enigmapython.Utils import Utils

# Import from python ecosystem
import logging
import sys


# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Setup Enigma D components (compared to other machine types, Enigma D doesn't have a plugboard)
rotor1 = EnigmaZRotorI()
rotor2 = EnigmaZRotorI()
rotor3 = EnigmaZRotorI()
reflector = ReflectorZUKW()
etw = EnigmaZEtw()

# Setup Enigma D machine
enigma = EnigmaZ(rotor3, rotor2, rotor1, reflector, etw, True)



# Test the Enigma machines
if __name__ == "__main__":
      

      scrambled_string_from_enigma = enigma.input_string('0'*810)
      scrambled_string_from_website = '37552131596831199881743162995855654144312947347656538571243198121563589618884321981215635458851124396565915818745581492416234885967453747991888615275145689752511631488553745283692366433898989613484395911899538591189953838566839722961488932382463397477489592987556954743799178393242723623699698749288581766297748826151763156883852674317999896299569849656899588628831326982565814628991785432412286285437459531961856662975642887722417492466954742884792347314732533231239141333124715874558149212631985658539956443418231585929314847322187415857474848529275745313437868688272488261517647422496981474837325874988649296565411866743179998216537885989319594385911262631145689752533977239176991779938332522361447428995985911954731735632541985898164436961378939358881324335342336439624531984892154143487445314911333124715149'
      #print(scrambled_string_from_enigma)
      print("Rotors[0].position: {}".format(enigma.rotors[0].position))
      print("Rotors[1].position: {}".format(enigma.rotors[1].position))
      print("Rotors[2].position: {}".format(enigma.rotors[2].position))
      print("Reflector.position: {}".format(enigma.reflector.position))
      scrambled_string_from_enigma += enigma.input_string('0')
      print("Rotors[0].position: {}".format(enigma.rotors[0].position))
      print("Rotors[1].position: {}".format(enigma.rotors[1].position))
      print("Rotors[2].position: {}".format(enigma.rotors[2].position))
      print("Rotors[2].double_step_triggered: {}".format(enigma.rotors[2].double_step_triggered))
      print("Reflector.position: {}".format(enigma.reflector.position))
      #scrambled_string_from_enigma += enigma.input_string('0')
      #print("Rotors[0].position: {}".format(enigma.rotors[0].position))
      #print("Rotors[1].position: {}".format(enigma.rotors[1].position))
      #print("Rotors[2].position: {}".format(enigma.rotors[2].position))
      #print("Reflector.position: {}".format(enigma.reflector.position))
      print(Utils.find_divergence(scrambled_string_from_enigma, scrambled_string_from_website))


      print('0'*811)

   
     