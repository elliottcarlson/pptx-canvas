"""
==========
CanvasText
==========
"""
class CanvasText(object):
    """
    [NoInterfaceObject]
    interface CanvasText {
        // text (see also the CanvasPathDrawingStyles and
        // CanvasTextDrawingStyles interfaces)
        void fillText(DOMString text, unrestricted double x, unrestricted double
            y, optional unrestricted double maxWidth);
        void strokeText(DOMString text, unrestricted double x, unrestricted
            double y, optional unrestricted double maxWidth);
        TextMetrics measureText(DOMString text);
    };
    """

    def __init__(self):
        if type(self) == CanvasText:
            raise Exception('<CanvasText> must be subclassed.')

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
        pass

    def measureText(self, text):
        """
        Returns a TextMetrics object with the metrics of the given text in the
        current font.
        """
        pass
