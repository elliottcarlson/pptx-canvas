import unittest
from canvas.lib.color import Color

class ColorTest(unittest.TestCase):

    def test_full_hex_color(self):
        color = Color('red')
        self.assertEqual(color.hex, 'ff0000')

if __name__ == "__main__" and __package__ is None:
    unittest.main()  # pragma: no cover

