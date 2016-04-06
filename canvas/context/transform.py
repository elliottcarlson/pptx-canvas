"""
===============
CanvasTransform
===============
"""
import math

class CanvasTransform(object):
    """
    [NoInterfaceObject]
    interface CanvasTransform {
        // transformations (default transform is the identity matrix)
        void scale(unrestriucted double x, unrestricted double y);
        void rotate(unrestricted double angle);
        void translate(unrestricted double x, unrestricted double y);
        void transform(unrestricted double a, unrestricted double b,
            unrestricted double c, unrestricted double d, unrestricted double e,
            unrestricted double f);

        [NewObject] DomMatrix getTransform();
        void setTransform(unrestricted double a, unrestricted double b,
            unrestricted double c, unrestricted double d, unrestricted double e,
            unrestricted double f);
        void setTransform(optional DOMMatrixInit matrix);
        void resetTransform();
    };
    """

    _matrix = [ 1, 0, 0, 1, 0, 0 ]

    def __init__(self):
        if type(self) == CanvasTransform:
            raise Exception('<CanvasTransform> must be subclassed.')

    def _matrix_multiply(self, t, m):
        """
        3x3 matrix multiplier
        """
        x11 = t[0] * m[0] + t[2] * m[1]
        x21 = t[1] * m[0] + t[3] * m[1]
        x12 = t[0] * m[2] + t[2] * m[3]
        x22 = t[1] * m[2] + t[3] * m[3]
        x13 = t[0] * m[4] + t[2] * m[5] + t[4]
        x23 = t[1] * m[4] + t[3] * m[5] + t[5]

        return [ x11, x21, x12, x22, x13, x23 ]


    def scale(self, x, y):
        """
        Changes the current transformation matrix to apply a scaling
        transformation with the given characteristics.
        """
        _matrix = [ x, 0 , 0, y, 0, 0 ]
        self._matrix = self._matrix_multiply(self._matrix, _matrix)

    def rotate(self, angle):
        """
        Changes the current transformation matrix to apply a rotation
        transformation with the given characteristics. The angle is in radians.
        """
        _sin = math.sin(angle)
        _cos = math.cos(angle)

        _matrix = [ _cos, _sin, -_sin, _cos, 0, 0 ]
        self._matrix = self._matrix_multiply(self._matrix, _matrix)

    def translate(self, x, y):
        """
        Changes the current transformation matrix to apply a translation
        transofrmation with the given characteristics.
        """
        xy = (int(x), int(y))
        _matrix = [ 1, 0, 0, 1, xy[0], xy[1] ]
        self._matrix = self._matrix_multiply(self._matrix, _matrix)

    def transform(self, a, b, c, d, e, f):
        """
        Changes the current transformation matrix to apply the matrix given by
        the arguments as described below.
        """
        pass

    def getTransform(self):
        """
        Returns a copy of the current transformation matrix, as a newly created
        DOMMatrix object.
        """
        pass

    def setTransform(self, a, b, c, d, e, f):
        """
        Changes the current transformation matrix to the matrix given by the
        arguments as described below.
        """
        pass

    def setTransform(self, matrix):
        """
        Changes the current transformation matrix to the matrix represented by
        the passed DOMMatrixInit dictionary.
        """
        pass

    def resetTransform(self):
        """
        Changes the current transformation matrix to the identity transform.
        """
        pass


