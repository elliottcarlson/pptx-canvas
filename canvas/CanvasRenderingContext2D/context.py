"""
========================
CanvasRenderingContext2D
========================
"""
from .state import CanvasState
from .transform import CanvasTransform
from .compositing import CanvasCompositing
from .imagesmoothing import CanvasImageSmoothing
from .fillstrokestyles import CanvasFillStrokeStyles
from .shadowstyles import CanvasShadowStyles
from .rect import CanvasRect
from .drawpath import CanvasDrawPath
from .userinterface import CanvasUserInterface
from .text import CanvasText
from .drawimage import CanvasDrawImage
from .hitregion import CanvasHitRegion


from .gradient import CanvasGradient
from .pattern import CanvasPattern
from .shape import Shape

from pprint import pprint
from lxml.builder import ElementMaker

class CanvasRenderingContext2D(CanvasState, CanvasTransform, CanvasCompositing,
        CanvasImageSmoothing, CanvasFillStrokeStyles, CanvasShadowStyles,
        CanvasRect, CanvasDrawPath, CanvasUserInterface, CanvasText,
        CanvasDrawImage, CanvasHitRegion):
    ## OpenXML NameSpace map
    nsmap = {
        'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    }

    '''
    Implements a HTML <canvas> interface to drawing on PresentationML/DrawingML
    based PPTX slides.
    '''
    def __init__(self, canvas):
        self._canvas = canvas

        pprint(" -- SLIDE: --")
        pprint(self._canvas._slide)

        """Construct a Canvas instance."""
        self._shadowColor = '000000'
        self._shadowBlur = 0
        self._shadowOffsetX = 0
        self._shadowOffsetY = 0

        self._lineWidth = 12700

    @property
    def canvas(self):
        """
        A read-only reference to the PPTXCanvas object this Context exists on.
        """
        return self._canvas

    @property
    def lineWidth(self):
        '''
        Returns the current line width value.
        Default value is 12700 EMU.
        '''
        return self._lineWidth

    @lineWidth.setter
    def lineWidth(self, val):
        '''
        '''
        self._lineWidth = val
