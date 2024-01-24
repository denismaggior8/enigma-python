from RotorWiringI import RotorWiringI
from RotorWiringII import RotorWiringII
from RotorWiringIII import RotorWiringIII
from PlugboardPassthrough import PlugboardPassthrough
from ReflectorUKWB import ReflectorUKWB
from EnigmaThreeRotors import EnigmaThreeRotors
from EtwPassthrough import EtwPassthrough

import unittest

suite = unittest.TestLoader().discover(start_dir="tests",pattern="*_test*.py")
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unittest.main()