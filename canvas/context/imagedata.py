"""
===============
CanvasImageData
===============
"""
from canvas.lib.uint8clampedarray import Uint8ClampedArray
from canvas.lib.imagedata import ImageData

class IndexSizeError(Exception):
    pass

class InvalidStateError(Exception):
    pass

class CanvasImageData(object):
    """
    [NoInterfaceObject]
    interface CanvasImageData {
        // pixel manipulation
        ImageData createImageData(double sw, double sh);
        ImageData createImageData(ImageData imagedata);
        ImageData getImageData(double sx, double sy, double sw, double sh);
        void putImageData(ImageData imagedata, double dx, double dy);
        void putImageData(ImageData imagedata, double dx, double dy, double
            dirtyX, double dirtyY, double dirtyWidth, double dirtyHeight);
    };
    """

    def __init__(self):
        if type(self) == CanvasImageData:
            raise Exception('<CanvasImageData> must be subclassed.')

    def createImageData(self, sw=0, sh=0, imagedata=None):
        """
        Returns an ImageData object with the given dimensions. All the pixels in
        the returned object are transparent black.

        Throws an IndexSizeError exception if either of the width or height
        arguments are zero.
        """
        if isinstance(imagedata, ImageData):
            sw = imagedata.width
            sh = imagedata.height

        if sw is 0 or sh is 0:
            raise IndexSizeError()

        return ImageData(sw, sh)
        pass

    def getImageData(self, sx, sy, sw, sh):
        pass

    def putImageData(self, imagedata, dx, dy, dirtyX=None, dirtyY=None,
            dirtyWidth=None, dirtyHeight=None):
        if not isinstance(imagedata, ImageData):
            raise InvalidStateError()
        pass
