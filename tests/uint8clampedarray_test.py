"""Tests for Canvas.CanvasRenderingContext2D.Uint8ClampedArray"""

import unittest
from canvas.CanvasRenderingContext2D.uint8clampedarray import Uint8ClampedArray

class Uint8ClampedArrayTest(unittest.TestCase):
    """Tests for Uint8ClampedArray"""

    def setUp(self):
        self.clampedArray = Uint8ClampedArray(3)
        self.clampedArray[0] = -17 # Should get clamped at 0
        self.clampedArray[1] = 93  # Should remain at 93
        self.clampedArray[2] = 350 # Should get clamped at 255

    def test_is_instance(self):
        self.assertTrue(isinstance(self.clampedArray, Uint8ClampedArray))

    def test_get_values(self):
        self.assertEqual(self.clampedArray[0], 0)
        self.assertEqual(self.clampedArray[1], 93)
        self.assertEqual(self.clampedArray[2], 255)

    def test_array_len(self):
        self.assertEqual(len(self.clampedArray), 3)

if __name__ == "__main__" and __package__ is None:
    unittest.main()  # pragma: no cover

