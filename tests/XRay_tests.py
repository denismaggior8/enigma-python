import unittest
from unittest.mock import patch, MagicMock
from rich.text import Text

from enigmapython.EnigmaKRotorI import EnigmaKRotorI
from enigmapython.EnigmaKRotorII import EnigmaKRotorII
from enigmapython.EnigmaKRotorIII import EnigmaKRotorIII
from enigmapython.ReflectorUKW_EnigmaCommercial import ReflectorUKW_EnigmaCommercial
from enigmapython.EtwQWERTZ import EtwQWERTZ
from enigmapython.EnigmaK import EnigmaK
from enigmapython.XRay import XRay

class TestXRay(unittest.TestCase):
    def test_render_enigma_xray(self):
        """Test that XRay.render_enigma_xray returns a Text object with expected content"""
        # Setup Enigma K
        rotor1 = EnigmaKRotorI(0, 0)
        rotor2 = EnigmaKRotorII(0, 0)
        rotor3 = EnigmaKRotorIII(0, 0)
        reflector = ReflectorUKW_EnigmaCommercial()
        etw = EtwQWERTZ()
        
        enigma = EnigmaK(rotor1, rotor2, rotor3, reflector, etw, True)
        
        # Process a char to ensure journals are populated
        enigma.input_char('a')
        
        # Mock Console to prevent actual printing
        with patch('enigmapython.XRay.Console') as MockConsole:
            # Configure the mock to return a mock console instance
            mock_console_instance = MagicMock()
            MockConsole.return_value = mock_console_instance
            
            # Call the method under test
            result = XRay.render_enigma_xray(enigma)
            
            # Assertions
            self.assertIsInstance(result, Text)
            
            # Check content of the rendered text
            rendered_string = result.plain
            self.assertIn("UKW", rendered_string)
            self.assertIn("Rotor", rendered_string)
            self.assertIn("ETW", rendered_string)
            self.assertIn("PLUGBOARD", rendered_string)
            self.assertIn("Lamp", rendered_string)
            self.assertIn("Key", rendered_string)
            self.assertIn("Ring", rendered_string)
            self.assertIn("Pos", rendered_string)
            
            # Verify console.print was called
            mock_console_instance.print.assert_called_once()
            
if __name__ == '__main__':
    unittest.main()
