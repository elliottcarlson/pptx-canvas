"""
==========
CanvasRect
==========
"""
from .shape import Shape
from pprint import pprint

class CanvasRect(object):
    """
    [NoInterfaceObject]
    interface CanvasRect {
        // rects
        void clearRect(unrestricted double x, unrestricted double y,
            unrestricted double w, unrestricted double h);
        void fillRect(unrestricted double x, unrestricted double y,
            unrestricted double w, unrestricted double h);
        void strokeRect(unrestricted double x, unrestricted double y,
            unrestricted double w, unrestricted double h);
    };
    """

    def __init__(self):
        if type(self) == CanvasRect:
            raise Exception('<CanvasRect> must be subclassed.')

    def clearRect(self, x, y, width, height):
        pass

    def fillRect(self, x, y, width, height):
        """
        Draw a filled rectangle at (x, y) position whose size is determined by
        width and height and whose style is determined by the fillStyle
        attribute.

        Parameters
        ----------
        x : int
            The x axis of the coordinate for the rectangle starting point.
        y : int
            The y axis of the coordinate for the rectangle starting point.
        width : int
            The rectangle's width.
        height : int
            The rectangle's height.
        """
        shapes = self._canvas._slide._element.find('.//p:spTree', namespaces=self.nsmap)
        new_shape = Shape()

        shp = new_shape.prstGeom('rect', x, y, width - x, height - y)
        shp.spPr.append(new_shape._a.ln(new_shape._a.solidFill(new_shape.color(srgbClr=self.strokeStyle)), w=str(self.lineWidth)))


        #shp.fill.solid()
        #shp.fill.fore_color.rgb = RGBColor.from_string('3C2F80')

        pprint(shp)
        shapes.append(shp)

        pass

    def strokeRect(self, x, y, width, height):
        pass
