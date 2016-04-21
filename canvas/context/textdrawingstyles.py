"""
=======================
CanvasTextDrawingStyles
=======================
"""
from canvas.lib.cssfontparse import CSSFontParse

class CanvasTextDrawingStyles(object):
    """
    [NoInterfaceObject]
    interface CanvasTextDrawingStyles {
        // text
        attribute DOMString font; // (default 10px sans-serif)
        attribute CanvasTextAlign textAlign; // (default: "start")
        attribute CanvasTextBaseline textBaseline; // (default: "alphabetic")
        attribute CanvasDirection direction; // (default: "inherit")
    };
    """

    _font = None
    _textAlign = 'start'
    _textBaseline = 'alphabetic'
    _direction = 'inherit'

    def __init__(self):
        if type(self) == CanvasTextDrawingStyles:
            raise Exception('<CanvasTextDrawingStyles> must be subclassed.')

        self._font = CSSFontParse('10pt sans-serif')

    @property
    def font(self):
        """
        Return the serialized form  of the current font, without displaying
        """
        return str(self._font)

    @font.setter
    def font(self, val):
        """
        Set the current font based on the CSS <font> short-hand format.
        """
        self._font = CSSFontParse(val)

    def fillText(self, text, x, y, maxWidth=None):
        """
        Fills the given text at the given position. If a maximum width is
        provided, the text will be scaled to fit that width if necessary.
        """
        pass

    def strokeText(self, text, x, y, maxWidth=None):
        """
        Strokes the given text at the given position. If a maximum width is
        provided, the text will be scaled to fit that width if necessary.
        """
        shapes = self._canvas._slide._element.find('.//p:spTree', namespaces=self.nsmap)
        shape = Shape()

        txBody = shape.text(text, x, y, 1000, 1000) #self._canvas._slide_width, self._canvas._slide_height)
        shapes.append(txBody)
        pass

    def measureText(self, text):
        """
        Returns a TextMetrics object with the metrics of the given text in the
        current font.
        """
        pass
