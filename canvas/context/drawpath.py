"""
==============
CanvasDrawPath
==============
"""
from .path import CanvasPath

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

    def __init__(self):
        if type(self) == CanvasDrawPath:
            raise Exception('<CanvasDrawPath> must be subclassed.')

    def beginPath(self):
        """
        The beginPath() method must empty the list of subpaths in the context's
        current default path so that the it once again has zero subpaths.
        """
        self._path = []

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
        if path is None:
            path = self._path
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
