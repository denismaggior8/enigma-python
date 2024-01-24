from RotorWiringI import RotorWiringI
from RotorWiringII import RotorWiringII
from RotorWiringIII import RotorWiringIII
from PlugboardPassthrough import PlugboardPassthrough
from ReflectorUKWB import ReflectorUKWB
from EnigmaThreeRotors import EnigmaThreeRotors
from EtwPassthrough import EtwPassthrough
from EnigmaThreeRotors import EnigmaThreeRotors, TestEnigma
import unittest

suite = unittest.TestLoader().loadTestsFromModule(TestEnigma)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unittest.main()