"""
======================
CanvasFillStrokeStyles
======================
"""
from .gradient import CanvasGradient
from .pattern import CanvasPattern
from canvas.lib.color import Color

class CanvasFillStrokeStyles(object):
    """
    [NoInterfaceObject]
    interface CanvasFillStrokeStyles {
        // colours and styles (see also the CanvasPathDrawingStyles and
        // CanvasTextDrawingStyles interfaces)
        attribute (DOMString or CanvasGradient or CanvasPattern) strokeStyle;
            // (default black)
        attribute (DOMString or CanvasGradient or CanvasPattern) fillStyle;
            // (default black)
        CanvasGradient createLinearGradient(double x0, double y0, double x1,
            double y1);
        CanvasGradient createRadialGradient(double x0, double y0, double r0,
            double x1, double y1, double r1);
        CanvasPattern? createPattern(CanvasImageSource image,
            [TreatNullAs=EmptyString] DOMString repetition);
    };
    """
    _strokeStyle = Color('black')
    _fillStyle = Color('black')

    def __init__(self):
        if type(self) == CanvasFillStrokeStyles:
            raise Exception('<CanvasFillStrokeStyles> must be subclassed.')

    @property
    def strokeStyle(self):
        """
        Returns the current style used for stroking shapes.
        """
        return self._strokeStyle

    @strokeStyle.setter
    def strokeStyle(self, val):
        """
        Can be set, to change the stroke style.

        The style can be either a string containing a CSS colour, or a
        CanvasGradient or CanvasPattern object. Invalid values are ignored.
        """
        if (isinstance(val, CanvasGradient) or
                isinstance(val, CanvasPattern) or
                isinstance(val, Color)):
            self._strokeStyle = val
        else:
            self._strokeStyle=  Color(val)

    @property
    def fillStyle(self):
        """
        Returns the current style used for filling shapes.
        """
        return self._fillStyle

    @fillStyle.setter
    def fillStyle(self, val):
        """
        Can be set, to change the fill style.

        The style can be either a string containing a CSS colour, or a
        CanvasGradient or CanvasPattern object. Invalid values are ignored.
        """
        if (isinstance(val, CanvasGradient) or
                isinstance(val, CanvasPattern) or
                isinstance(val, Color)):
            self._fillStyle = val
        else:
            self._fillStyle = Color(val)

    def createLinearGradient(self, x0, y0, x1, y1):
        """
        """
        return CanvasGradient()

    def createRadialGradient(self, x0, y0, r0, x1, y1, r1):
        """
        """
        return CanvasGradient()

    def createPattern(self, source, repetition='repeat'):
        """
        """
        return CanvasPattern()
