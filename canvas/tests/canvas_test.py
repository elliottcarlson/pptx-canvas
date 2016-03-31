"""Tests for letsencrypt.client."""
import os
import shutil
import tempfile
import unittest

from canvas import Canvas

class CanvasTest(unittest.TestCase):
    """Tests for canvas."""

    def setUp(self):
        self.canvas = Canvas(None, 10, 10)

    def test_is_instance(self):
        self.assertTrue(isinstance(self.canvas, Canvas))

if __name__ == "__main__" and __package__ is None:
    unittest.main()  # pragma: no cover
