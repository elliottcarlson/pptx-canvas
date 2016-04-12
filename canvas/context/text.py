"""
==========
CanvasText
==========
"""
from .shape import Shape

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
