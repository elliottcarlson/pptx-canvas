"""
===============
CanvasTransform
===============
"""
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

    _matrix = []

    def __init__(self):
        if type(self) == CanvasTransform:
            raise Exception('<CanvasTransform> must be subclassed.')

    def scale(self, x, y):
        """
        Changes the current transformation matrix to apply a scaling
        transformation with the given characteristics.
        """
        pass

    def rotate(self, angle):
        """
        Changes the current transformation matrix to apply a rotation
        transformation with the given characteristics. The angle is in radians.
        """
        pass

    def translate(self, x, y):
        """
        Changes the current transformation matrix to apply a tranlation
        transofrmation with the given characteristics.
        """
        pass

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


