
from PlugboardPassthrough import PlugboardPassthrough
from ReflectorUKWB import ReflectorUKWB
from EnigmaM3 import EnigmaM3
from EtwPassthrough import EtwPassthrough
import unittest


if __name__ == "__main__":   
    suite = unittest.TestLoader().discover(start_dir="tests",pattern="*_test*.py")
    unittest.TextTestRunner(verbosity=2).run(suite)