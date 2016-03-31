"""
==================
CanvasShadowStyles
==================
"""
from colour import Color

class CanvasShadowStyles(object):
    """
    [NoInterfaceObject]
    interface CanvasShadowStyles {
        // shadows
        attribute unrestricted double shadowOffsetX; // (default 0)
        attribute unrestricted double shadowOffsetY; // (default 0)
        attribute unrestricted double shadowBlur; // (default 0)
        attribute DOMString shadowColor; // (default transparent black)
    };
    """
    _shadowOffsetX = 0
    _shadowOffsetY = 0
    _shadowBlur = 0
    _shadowColor = Color('black')

    def __init__(self):
        if type(self) == CanvasShadowStyles:
            raise Exception('<CanvasShadowStyles> must be subclassed.')

    @property
    def shadowOffsetX(self):
        """
        """
        return self._shadowOffsetX

    @shadowOffsetX.setter
    def shadowOffsetX(self, val):
        """
        """
        if (isinstance(val, int) or
                isinstance(val, float)):
            self._shadowOffsetX = round(val)

    @property
    def shadowOffsetY(self):
        """
        """
        return self._shadowOffsetY

    @shadowOffsetY.setter
    def shadowOffsetY(self, val):
        """
        """
        if (isinstance(val, int) or
                isinstance(val, float)):
            self._shadowOffsetY = round(val)

    @property
    def shadowBlur(self):
        """
        """
        return self._shadowBlur

    @shadowBlur.setter
    def shadowBlur(self, val):
        """
        """
        if (isinstance(val, int) and
                val > 0):
            self._shadowBlur = val

    @property
    def shadowColor(self):
        """
        """
        return self._shadowColor.hex

    @shadowColor.setter
    def shadowColor(self, val):
        """
        """
        try:
            self._shadowColor = Color(val)
        except:
            pass

