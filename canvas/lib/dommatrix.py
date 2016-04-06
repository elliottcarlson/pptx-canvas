"""
=================
DOMMatrixReadOnly
=================
"""
class DOMMatrixReadOnly(array):

    _default_matrix = {
        'm11': 1, 'm12': 0, 'm13': 0, 'm14': 0,
        'm21': 0, 'm22': 1, 'm23': 0, 'm24': 0,
        'm31': 0, 'm32': 0, 'm33': 1, 'm34': 0,
        'm41': 0, 'm42': 0, 'm43': 0, 'm44': 1
    }

    _is2D = False
    _isIdentity = False

    def __new__(cls, size=0):
        self._matrix = self._default_matrix


        return array.__new__(cls, 'B', [0] * size)

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


    def multiplySelf(self, other):
        pass

    def preMultiplySelf(self, other):
        pass

    def translateSelf(self, tx, ty, tx=0):
        pass

    def scaleSelf(self, scale, originX=0, originY=0):
        pass

    def scale3dSelf(self, scale, originX=0, originY=0, originZ=0):
        pass

    def scaleNonUniformSelf(self, scaleX, scaleY=1, scaleZ=1, originX=0,
            originY=0, originZ=0):
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


