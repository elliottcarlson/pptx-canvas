"""
==========
CanvasPath
==========
"""
class CanvasPath(object):
    """
    [NoInterfaceObject, Exposed=(Window,Worker)]
    interface CanvasPath {
        // shared path API methods
        void closePath();
        void moveTo(unrestricted double x, unrestricted double y);
        void lineTo(unrestricted double x, unrestricted double y);
        void quadraticCurveTo(unrestricted double cpx, unrestricted double cpy,
            unrestricted double x, unrestricted double y);
        void bezierCurveTo(unrestricted double cp1x, unrestricted double cp1y,
            unrestricted double cp2x, unrestricted double cp2y, unrestricted
            double x, unrestricted double y);
        void arcTo(unrestricted double x1, unrestricted double y1, unrestricted
            double x2, unrestricted double y2, unrestricted double radius);
        void arcTo(unrestricted double x1, unrestricted double y1, unrestricted
            double x2, unrestricted double y2, unrestricted double radiusX,
            unrestricted double radiusY, unrestricted double rotation);
        void rect(unrestricted double x, unrestricted double y, unrestricted
            double w, unrestricted double h);
        void arc(unrestricted double x, unrestricted double y, unrestricted
            double radius, unrestricted double startAngle, unrestricted double
            endAngle, optional boolean anticlockwise = false);
        void ellipse(unrestricted double x, unrestricted double y, unrestricted
            double radiusX, unrestricted double radiusY, unrestricted double
            rotation, unrestricted double startAngle, unrestricted double
            endAngle, optional boolean anticlockwise = false);
    };
    """

    def __init__(self):
        if type(self) == CanvasPath:
            raise Exception('<CanvasPath> must be subclassed.')

    def closePath(self):
        """
        Marks the current subpath as closed, and starts a new subpath with a
        point the same as the start and end of the newly closed subpath.
        """
        pass

    def moveTo(self, x, y):
        """
        Creates a new subpath with the given point.
        """
        pass

    def lineTo(self, x, y):
        """
        Adds the given point to the current subpath, connected to the previous
        one by a straight line.
        """
        pass

    def quadraticCurveTo(self, cpx, cpy, x, y):
        """
        Adds the given point to the current subpath, connected to the previous
        one by a quadratic Bezier curve with the given control point.
        """
        pass

    def bezierCurveTo(self, cp1x, cp1y, cp2x, cp2y, x, y):
        """
        Adds the given point to the current subpath, connected to the previous
        one by a cubic Bezier curve with the given control points.
        """
        pass

    def arcTo(self, x1, y1, x2, y2, radius, radius2=None, rotation=None):
        """
        Adds an arc with the given control points and radius to the current
        subpath, connected to the previous point by a straight line.

        If two radii are provided, the first controls the width of the arc's
        ellipse, and the second controls the height. If only one is provided, or
        if they are the same, the arc is from a circle. In the case of an
        ellipse, the rotation argument controls the clockwise inclination of the
        ellipse relative to the x-axis.

        Throws an IndexSizeError exception if the given radius is negative.

        https://html.spec.whatwg.org/images/arcTo1.png
        https://html.spec.whatwg.org/images/arcTo2.png
        https://html.spec.whatwg.org/images/arcTo3.png
        """
        pass

    def arc(self, x, y, startAngle, endAngle, anticlockwise=False):
        """
        Adds points to the subpath such that the arc described by the
        circumference of the circle described by the arguments, starting at the
        given start angle and ending at the given end angle, going in the given
        direction (defaulting to clockwise), is added to the path, connected to
        the previous point by a straight line.

        Throws an IndexSizeError exception if the given radius is negative.

        https://html.spec.whatwg.org/images/arc1.png
        """
        pass

    def ellipse(self, x, y, radiusX, radiusY, rotation, startAngle, endAngle,
            anticlockwise=False):
        """
        Adds points to the subpath such that the arc described by the
        circumference of the ellipse described by the arguments, starting at the
        given start angle and ending at the given end angle, going in the given
        direction (defaulting to clockwise), is added to the path, connected to
        the previous point by a straight line.

        Throws an IndexSizeError exception if the given radius is negative.
        """
        pass

    def rect(self, x, y, w, h):
        """
        Adds a new closed subpath to the path, representing the given rectangle.
        """
        pass
