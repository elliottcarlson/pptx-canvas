"""
=================
CanvasCompositing
=================
"""
class CanvasCompositing(object):
    """
    [NoInterfaceObject]
    interface CanvasCompositing {
        // compositing
        attribute unrestricted double globalAlpha; // (default 1.0)
        attribute DOMString globalCompositeOperation; // (default source-over)
    };
    """
    _globalAlpha = 1.0
    _globalCompositeOperation = 'source-over'

    def __init__(self):
        if type(self) == CanvasCompositing:
            raise Exception('<CanvasCompositing> must be subclassed.')

    @property
    def globalAlpha(self):
        """
        The globalAlpha attribute gives an alpha value that is applied to shapes
        and images before they are composited onto the output bitmap. The value
        must be in the range from 0.0 (fully transparent) to 1.0 (no additional
        transparency). If an attempt is made to set the attribute to a value
        outside this range, including Infinity and Not-a-Number (NaN) values,
        the attribute must retain its previous value. When the context is
        created, the globalAlpha attribute must initially have the value 1.0.
        """
        return self._globalAlpha

    @globalAlpha.setter
    def globalAlpha(self, val):
        if isinstance(val, float) and 0.0 < val < 1.0:
            self._globalAlpha = val

    @property
    def globalCompositeOperation(self):
        """
        The globalCompositeOperation attribute sets the current composition
        operator, which controls how shapes and images are drawn onto the output
        bitmap, once they have had globalAlpha and the current transformation
        matrix applied. The possible values are those defined in the Compositing
        and Blending specification, and include the values source-over and copy.

        On setting, if the user agent does not recognise the specified value, it
        must be ignored, leaving the value of globalCompositeOperation
        unaffected. Otherwise, the attribute must be set to the given new value.
        """
        return self._globalCompositeOperation

    @globalCompositeOperation.setter
    def globalCompositeOperation(self, val):
        if val in ['clear', 'copy', 'source-over', 'destination-over',
                'source-in', 'destination-in', 'source-out', 'destination-out',
                'source-atop', 'destination-atop', 'xor', 'lighter',
                'plus-darker', 'plus-lighter']:
            self._globalCompositeOperation = val

