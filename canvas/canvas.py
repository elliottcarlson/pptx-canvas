"""
======
Canvas
======

HTML Canvas compatbile interface to drawing on PPTX slides.
"""
from .CanvasRenderingContext2D import CanvasRenderingContext2D

class Canvas(object):
    def __init__(self, slide, height, width):
        """
        Create a new Canvas interface to a provided python-pptx `Slide`.

        Parameters
        ----------
        slide : Slide
            python-pptx Slide
        height : int
            Height of Slide in EMUs
        width : int
            Width of Slide in EMUs
        """
        self._slide = slide
        self._slide_height = height
        self._slide_width = width

    def getContext(self, contextType):
        """
        Create a new Context to work with.

        This will build a new PPTX Shape to work with.

        Parameters
        ----------
        contextType : str
            The type of context to use. `2d` is the only available option.
        """
        if contextType is '2d':
            return CanvasRenderingContext2D(self)

        return null

    def  probablySupportsContext(self, contextType):
        """
        Return boolean value if the Canvas supports the requested contextType.

        Parameters
        ----------
        contextType : str
            The type of context to check.
        """
        if contextType is '2d':
            return True

        return False
