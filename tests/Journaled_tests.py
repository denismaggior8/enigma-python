from enigmapython.EnigmaISonderRotorI import EnigmaISonderRotorI
from enigmapython.EnigmaISonderRotorII import EnigmaISonderRotorII
from enigmapython.EnigmaISonderRotorIII import EnigmaISonderRotorIII
from enigmapython.PlugboardPassthrough import PlugboardPassthrough
from enigmapython.Journaled import Journaled
from enigmapython.ReflectorSonderUKW import ReflectorSonderUKW
from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.EnigmaISonder import EnigmaISonder
from enigma.machine import EnigmaMachine

from string import ascii_lowercase
import random
import logging
import unittest
import sys

class TestJournaled(unittest.TestCase):

    def test_init_journaled(self):
        journaled = Journaled()
        self.assertEqual(journaled.journal,[],"Journal has not been inizialized correctly")

if __name__ == "__main__":
    unittest.main()