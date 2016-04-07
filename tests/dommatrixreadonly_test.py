"""Tests for Canvas.lib.DOMMatrixReadOnly"""

import unittest
from canvas.lib.dommatrixreadonly import DOMMatrixReadOnly

class DOMMatrixReadOnlyTest(unittest.TestCase):
    """Tests for DOMMatrixReadOnly"""

    matrix_args_2d = [ 1, 2, 3, 4, 5, 6 ]
    matrix_args_3d = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ]
    matrix_args_identity = [ 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ]

    def setUp(self):
        self.matrix_2d = DOMMatrixReadOnly(*self.matrix_args_2d)
        self.matrix_3d = DOMMatrixReadOnly(*self.matrix_args_3d)

    def test_is_instance_2d(self):
        self.assertIsInstance(self.matrix_2d, DOMMatrixReadOnly)

    def test_is_instance_3d(self):
        self.assertIsInstance(self.matrix_3d, DOMMatrixReadOnly)

    def test_is_2d_matrix(self):
        self.assertTrue(self.matrix_2d.is2D)

    def test_is_3d_matrix(self):
        self.assertFalse(self.matrix_3d.is2D)

    def test_typeerror_on_bad_instanciation(self):
        with self.assertRaises(TypeError):
            _matrix = DOMMatrixReadOnly(None)

    def test_identity(self):
        _matrix = DOMMatrixReadOnly(*self.matrix_args_identity)
        self.assertTrue(_matrix.isIdentity)

    def test_no_identity(self):
        self.assertFalse(self.matrix_2d.isIdentity)
        self.assertFalse(self.matrix_3d.isIdentity)

    def test_readonly_matrix_properties(self):
        with self.assertRaises(AttributeError):
            self.matrix_2d.m11 = None

    def test_readonly_is2d_property(self):
        with self.assertRaises(AttributeError):
            self.matrix_2d.is2D = None

    def test_readonly_identity_property(self):
        with self.assertRaises(AttributeError):
            self.matrix_2d.isIdentity = None

if __name__ == "__main__" and __package__ is None:
    unittest.main()  # pragma: no cover

