"""
==============
CanvasDrawPath
==============

See `CanvasPath` in path.py
"""
from collections import OrderedDict
from .path import CanvasPath
from .shape import Shape

class CanvasDrawPath(CanvasPath):
    """
    [NoInterfaceObject]
    interface CanvasDrawPath {
        // path API (see also CanvasPath)
        void beginPath();
        void fill(optional CanvasFillRule fillRule = "nonzero");
        void fill(Path2D path, optional CanvasFillRule fillRule = "nonzero");
        void stroke();
        void stroke(Path2D path);
        void clip(optional CanvasFillRule fillRule = "nonzero");
        void clip(Path2D path, optional CanvasFillRule fillRule = "nonzero");
        void resetClip();
        boolean isPointInPath(unrestricted double x, unrestricted double y, optional CanvasFillRule fillRule = "nonzero");
        boolean isPointInPath(Path2D path, unrestricted double x, unrestricted double y, optional CanvasFillRule fillRule = "nonzero");
        boolean isPointInStroke(unrestricted double x, unrestricted double y);
        boolean isPointInStroke(Path2D path, unrestricted double x, unrestricted double y);
    };
    """
    _paths = [OrderedDict()]

    def __init__(self):
        if type(self) == CanvasDrawPath:
            raise Exception('<CanvasDrawPath> must be subclassed.')

    def beginPath(self):
        """
        The beginPath() method must empty the list of subpaths in the context's
        current default path so that the it once again has zero subpaths.
        """
        self._paths.append(OrderedDict())

    def fill(self, path=None, fillRule='nonzero'):
        """
        Fills the subpaths of the current default path or the given path with
        the current fill style, obeying the given fill rule.
        """
        if path is None:
            path = self._path
        pass

    def stroke(self, path=None):
        """
        Strokes the subpaths of the current default path or the given path with
        the current stroke style.
        """
        """
        shapes = self._canvas._slide._element.find('.//p:spTree', namespaces=self.nsmap)
        shape = Shape()

        prstGeom = shape.prstGeom('rect', x, y, width - x, height - y)
        solidFill = shape._a.solidFill(shape.color(srgbClr=self.fillStyle.hex))
        prstGeom.spPr.append(solidFill)

        shapes.append(prstGeom)
        """
        shapes = self._canvas._slide._element.find('.//p:spTree', namespaces=self.nsmap)
        shape = Shape()

        custGeom = shape.custGeom(0, 0, self._canvas._slide_width, self._canvas._slide_height)
        pathList = shape._a.pathLst()

        for paths in self._paths:

            path = shape._a.path()

            for command, attr in paths.items():

                if command is 'moveTo':
                    action = shape._a.moveTo()
                elif command is 'lnTo':
                    action = shape._a.lnTo()
                else:
                    pass

                pt = shape._a.pt(**dict([a, str(x)] for a, x in attr.items()))
                action.append(pt)
                path.append(action)

            pathList.append(path)

        custGeom = shape._a.custGeom(pathList)

        #custGeom.spPr.custGeom.append(pathList)
        shapes.append(
            shape._p.sp(
                shape._p.nvSpPr(
                    shape._p.cNvPr(id='1', name='Path 1'),
                    shape._p.cNvSpPr(),
                    shape._p.nvPr()
                ),
                shape._p.spPr(
                    shape._a.xfrm(
                        shape._a.off(x="0", y="0"),
                        shape._a.ext(cx="9144000", cy="5143500")
                    ),
                    custGeom,
                    shape._a.ln(
                        shape._a.solidFill(
                            shape._a.srgbClr(val=str(self.strokeStyle.hex))
                        )
                    , cap='flat', cmpd='sng', w=str(self.lineWidth))
                )
            )
        )

        #        custGeom)




        ln = shape._a.ln(shape._a.solidFill(shape._a.srgbClr(val=self.strokeStyle.hex)), cap="flat", cmpd="sng", w=str(self.lineWidth))
        #custGeom.spPr.append(ln)


            #test.append(pathList)


        #prstGeom = shape.prstGeom('rect', x, y, width - x, height - y)
        #solidFill = shape._a.solidFill(shape.color(srgbClr=self.fillStyle.hex))
        #prstGeom.spPr.append(solidFill)

        #shapes.append(prstGeom)



        #[OrderedDict([('moveTo', {'y': 127000, 'x': 127000}), ('lnTo', {'y': 1270000, 'x': 1270000})])]



        pass

    def clip(self, path=None, fillRule='nonzero'):
        """
        Further constrains the clipping region to the current default path or
        the given path, using the given fill rule to determine what points are
        in the path.
        """
        if path is None:
            path = self._path
        pass

    def resetClip(self):
        """
        Unconstrains the clipping region.
        """
        pass

    def isPointInPath(self, x, y, path=None, fillRule='nonzero'):
        """
        Returns true if the given point is in the current default path or the
        given path, using the given fill rule to determine what points are in
        the path.
        """
        if path is None:
            path = self._path
        pass

    def isPointInStroke(self, x, y, path=None):
        """
        Returns true if the given point would be in the region covered by the
        stroke of the current default path or the given path, given the current
        stroke style.
        """
        if path is None:
            path = self._path
        pass
