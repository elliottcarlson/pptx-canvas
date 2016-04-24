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

    _font = CSSFontParse('10pt sans-serif')
    _textAlign = 'start'
    _textBaseline = 'alphabetic'
    _direction = 'inherit'

    def __init__(self):
        if type(self) == CanvasTextDrawingStyles:
            raise Exception('<CanvasTextDrawingStyles> must be subclassed.')

    @property
    def font(self):
        """
        Return the serialized form  of the current font, without displaying
        """
        return str(self._font)

    @property
    def rawFont(self):
        return self._font

    @font.setter
    def font(self, val):
        """
        Set the current font based on the CSS <font> short-hand format.
        """
        self._font = CSSFontParse(val)

    @property
    def textAlign(self):
        """
        Returns the current value of the textAlign IDL attribute. The default
        value is "start".
        """
        return self._textAlign

    @textAlign.setter
    def textAlign(self, val):
        """
        Sets the textAlign IDL attribute when the value is one of "start",
        "end", "left", "right", or "center". Other values are ignored.
        """
        if val in ['start', 'end', 'left', 'right', 'center']:
            self._textAlign = val

    @property
    def textBaseline(self):
        """
        Returns the current value of the textBaseline IDL attribute. The default
        value is "alphabetic".
        """
        return self._textBaseline

    @textBaseline.setter
    def textBaseline(self, val):
        """
        Sets the textBaseline IDL attribute when the value is one of "top",
        "hanging", "middle", "alphabetic", "ideographic", or "bottom". Other
        values are ignored.
        """
        if val in ['top', 'hanging', 'middle', 'alphabetic', 'ideographic',
            'bottom']:
            self._textBaseline = val

    @property
    def direction(self):
        """
        Returns the current value of the direction IDL attribute. The default
        value is "inherit".
        """
        return self._direction

    @direction.setter
    def direction(self, val):
        """
        Sets the direction IDL attribute when the value is one of "ltr", "rtl",
        or "inherit". Other values are ignored.
        """
        if val in ['ltr', 'rtl', 'inherit']:
            self._direction = val
