"""
=================
DOMMatrixReadOnly
=================
"""
import numpy as np
import re

class DOMMatrixReadOnly(object):
    """
    [Constructor(sequence<unrestricted double> numberSequence),
        Exposed=(Window,Worker)]
    interface DOMMatrixReadOnly {
        // These attributes are simple aliases for certain elements of the 4x4
        // matrix
        readonly attribute unrestricted double a;
        readonly attribute unrestricted double b;
        readonly attribute unrestricted double c;
        readonly attribute unrestricted double d;
        readonly attribute unrestricted double e;
        readonly attribute unrestricted double f;

        readonly attribute unrestricted double m11;
        readonly attribute unrestricted double m12;
        readonly attribute unrestricted double m13;
        readonly attribute unrestricted double m14;
        readonly attribute unrestricted double m21;
        readonly attribute unrestricted double m22;
        readonly attribute unrestricted double m23;
        readonly attribute unrestricted double m24;
        readonly attribute unrestricted double m31;
        readonly attribute unrestricted double m32;
        readonly attribute unrestricted double m33;
        readonly attribute unrestricted double m34;
        readonly attribute unrestricted double m41;
        readonly attribute unrestricted double m42;
        readonly attribute unrestricted double m43;
        readonly attribute unrestricted double m44;

        readonly attribute boolean is2D;
        readonly attribute boolean isIdentity;

        // Immutable transform methods
        DOMMatrix translate(unrestricted double tx, unrestricted double ty,
            optional unrestricted double tz = 0);
        DOMMatrix scale(unrestricted double scale, optional unrestricted double
            originX = 0, optional unrestricted double originY = 0);
        DOMMatrix scale3d(unrestricted double scale, optional unrestricted
            double originX = 0, optional unrestricted double originY = 0,
            optional unrestricted double originZ = 0);
        DOMMatrix scaleNonUniform(unrestricted double scaleX, optional
            unrestricted double scaleY = 1, optional unrestricted double
            scaleZ = 1, optional unrestricted double originX = 0, optional
            unrestricted double originY = 0, optional unrestricted double
            originZ = 0);
        DOMMatrix rotate(unrestricted double angle, optional unrestricted double
            originX = 0, optional unrestricted double originY = 0);
        DOMMatrix rotateFromVector(unrestricted double x, unrestricted double y);
        DOMMatrix rotateAxisAngle(unrestricted double x, unrestricted double y,
            unrestricted double z, unrestricted double angle);
        DOMMatrix skewX(unrestricted double sx);
        DOMMatrix skewY(unrestricted double sy);
        DOMMatrix multiply(DOMMatrix other);
        DOMMatrix flipX();
        DOMMatrix flipY();
        DOMMatrix inverse();

        DOMPoint            transformPoint(optional DOMPointInit point);
        Float32Array        toFloat32Array();
        Float64Array        toFloat64Array();
                            stringifier;
    };
    """

    #_is2D = False

    def __init__(self, *args, **kwargs):
        """
        The DOMMatrixReadOnly(sequence<unrestricted double> numberSequence)
        constructor, when invoked, must run the following steps:

        If numberSequence has 6 elements
            * Set m11 element, m12 element, m21 element, m22 element, m41
              element, m42 element to the values of numberSequence in order
              starting with the first value. Furthermore, set m31 element, m32
              element, m13 element, m23 element, m43 element, m14 element, m24
              element, m34 element to 0 and m33 element, m44 element to 1.
            * Set is2D to true.
            * Return the new DOMMatrixReadOnly object.

        If numberSequence has 16 elements
            * Set m11 element to m44 element to the values of numberSequence in
              column-major order.
            * Set is2D to false.
            * Return the new DOMMatrixReadOnly object.

        Otherwise
            Throw a TypeError exception.

        Source: https://www.w3.org/TR/geometry-1/#dommatrixreadonly-constructors
        """
        from .dommatrix import DOMMatrix
        object.__setattr__(self, 'DOMMatrix', DOMMatrix)

        object.__setattr__(self, '_matrix', {
            'm11': 1, 'm12': 0, 'm13': 0, 'm14': 0,
            'm21': 0, 'm22': 1, 'm23': 0, 'm24': 0,
            'm31': 0, 'm32': 0, 'm33': 1, 'm34': 0,
            'm41': 0, 'm42': 0, 'm43': 0, 'm44': 1
        })

        if len(args) is 6:
            self._matrix['m11'] = args[0]
            self._matrix['m12'] = args[1]
            self._matrix['m21'] = args[2]
            self._matrix['m22'] = args[3]
            self._matrix['m41'] = args[4]
            self._matrix['m42'] = args[5]

            # Due to __setattr__ overloading in DOMMatrix
            object.__setattr__(self, '_is2D', True)

        elif len(args) is 16:
            self._matrix['m11'] = args[0]
            self._matrix['m12'] = args[1]
            self._matrix['m13'] = args[2]
            self._matrix['m14'] = args[3]
            self._matrix['m21'] = args[4]
            self._matrix['m22'] = args[5]
            self._matrix['m23'] = args[6]
            self._matrix['m24'] = args[7]
            self._matrix['m31'] = args[8]
            self._matrix['m32'] = args[9]
            self._matrix['m33'] = args[10]
            self._matrix['m34'] = args[11]
            self._matrix['m41'] = args[12]
            self._matrix['m42'] = args[13]
            self._matrix['m43'] = args[14]
            self._matrix['m44'] = args[15]

            # Due to __setattr__ overloading in DOMMatrix
            object.__setattr__(self, '_is2D', False)

        elif kwargs is not None and bool(kwargs):
            for key, value in kwargs.items():
                match = re.search(r'^m[1-4][1-4]$', key)
                if match and key in self._matrix:
                    self._matrix[key] = value
                else:
                    raise TypeError()

        else:
            raise TypeError()

    @property
    def m11(self):
        return self._matrix['m11']

    @property
    def m12(self):
        return self._matrix['m12']

    @property
    def m13(self):
        return self._matrix['m13']

    @property
    def m14(self):
        return self._matrix['m14']

    @property
    def m21(self):
        return self._matrix['m21']

    @property
    def m22(self):
        return self._matrix['m22']

    @property
    def m23(self):
        return self._matrix['m23']

    @property
    def m24(self):
        return self._matrix['m24']

    @property
    def m31(self):
        return self._matrix['m31']

    @property
    def m32(self):
        return self._matrix['m32']

    @property
    def m33(self):
        return self._matrix['m33']

    @property
    def m34(self):
        return self._matrix['m34']

    @property
    def m41(self):
        return self._matrix['m41']

    @property
    def m42(self):
        return self._matrix['m42']

    @property
    def m43(self):
        return self._matrix['m43']

    @property
    def m44(self):
        return self._matrix['m44']

    @property
    def a(self):
        return self._matrix['m11']

    @property
    def b(self):
        return self._matrix['m12']

    @property
    def c(self):
        return self._matrix['m21']

    @property
    def d(self):
        return self._matrix['m22']

    @property
    def e(self):
        return self._matrix['m41']

    @property
    def f(self):
        return self._matrix['m42']

    @property
    def is2D(self):
        return self._is2D

    @property
    def isIdentity(self):
        """
        Returns true if m12, m13, m14, m21, m23, m24, m31, m32, m34, m41, m42,
        m43 are 0 and m11, m22, m33, m44 are 1. Otherwise returns false.
        """
        _m = self._matrix

        if (_m['m12'] == _m['m13'] == _m['m14'] == _m['m21'] ==
            _m['m23'] == _m['m24'] == _m['m31'] == _m['m32'] ==
            _m['m34'] == _m['m41'] == _m['m42'] == _m['m42'] == 0) and (
            _m['m11'] == _m['m22'] == _m['m33'] == _m['m44'] == 1):
            return True

        return False

    def _np_array(self, other=None):
        if other is not None:
            _m = other._matrix
        else:
            _m = self._matrix

        return np.array([
            [ _m['m11'], _m['m12'], _m['m13'], _m['m14'] ],
            [ _m['m21'], _m['m22'], _m['m23'], _m['m24'] ],
            [ _m['m31'], _m['m32'], _m['m33'], _m['m34'] ],
            [ _m['m41'], _m['m42'], _m['m43'], _m['m44'] ]
        ])

    def translate(self, x, y):
        #from .dommatrix import DOMMatrix
        _other = self.DOMMatrix(1, 0, 0, 1, x, y)

        return self.multiply(_other)

    def scale(self, x, y):
        #from .dommatrix import DOMMatrix
        _other = self.DOMMatrix(x, 0, 0, 0, 0, y, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
        print(_other)
        return self.multiply(_other)

    def multiply(self, other):
        #from .dommatrix import DOMMatrix
        _m = np.dot(self._np_array(other), self._np_array())
        return self.DOMMatrix(*_m.flatten())

    def translateSelf(self, tx, ty, tz=0):
        pass

    def scale3d(self, scale, ox=0, oy=0, oz=0):
        pass

    def scaleNonUniform(self, sx, sy=1, sz=1, ox=0, oy=0, oz=0):
        #from .dommatrix import DOMMatrix
        if sx == 1.0 and sy == 1.0 and sz == 1.0:
            return self

        _other = self.DOMMatrix(**self._matrix)
        _other.translate(ox, oy) #, oz)

        if not self.is2D or sz != 1.0 or oz != 0:
            ## TODO Ensure3DMatrix
            _m2 = self.DOMMatrix(sx, 0, 0, 0, 0, sy, 0, 0, 0, 0, sz, 0, 0, 0, 0, 0)
        else:
            _m2 = self.DOMMatrix(sx, 0, 0, 0, sy, 0)

        _out = _m2.multiply(_other)
        _out2 = _out.translate(-ox, -oy) # , -oz)
        return _out2
        pass

    def rotateSelf(self, angle, originX=0, originY=0):
        pass

    def rotateFromVectorSelf(self, x, y):
        pass

    def rotateAxisAngleSelf(self, x, y, z, angle):
        pass

    def skewXSelf(self, sx):
        pass

    def skewYSelf(self, sy):
        pass

    def invertSelf(self):
        pass

    def setMatrixValue(self, transformList):
        pass

    def __str__(self):
        r = ""
        r = r + "[ %s, %s, %s, %s ],\n" % (self.m11, self.m12, self.m13, self.m14)
        r = r + "[ %s, %s, %s, %s ],\n" % (self.m21, self.m22, self.m23, self.m24)
        r = r + "[ %s, %s, %s, %s ],\n" % (self.m31, self.m32, self.m33, self.m34)
        r = r + "[ %s, %s, %s, %s ]\n" % (self.m41, self.m42, self.m43, self.m44)
        r = r + "\n"
        r = r + "a: %s\n" % self.a
        r = r + "b: %s\n" % self.b
        r = r + "c: %s\n" % self.c
        r = r + "d: %s\n" % self.d
        r = r + "e: %s\n" % self.e
        r = r + "f: %s\n" % self.f
        return r
