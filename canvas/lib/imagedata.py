"""
===============
CanvasImageData
===============
"""
from canvas.lib.uint8clampedarray import Uint8ClampedArray

class IndexSizeError(Exception):
    pass

class ImageData(object):
    """
    [Constructor(unsigned long sw, unsigned long sh),
    Constructor(Uint8ClampedArray data, unsigned long sw, optional unsigned long
    sh), Exposed=(Window,Worker)]
    interface ImageData {
        readonly attribute unsigned long width;
        readonly attribute unsigned long height;
        readonly attribute Uint8ClampedArray data;
    };

    Syntax

        ImageData ctx.createImageData(width, height);
        ImageData ctx.createImageData(imagedata);

    Parameters

        width
            The width to give the new ImageData object.

        height
            The height to give the new ImageData object.

        imagedata
            An existing ImageData object from which to copy the width and
            height. The image itself is not copied.

    Return value

        A new ImageData object with the specified width and height. The new
        object is filled with transparent black pixels.

    Errors thrown

        IndexSizeError
            Thrown if either of the width or height arguments are zero.
    """
    def __init__(self, sw=0, sh=0, data=None):
        if isinstance(data, ImageData):
            sw = data.width
            sh = data.height

        if sw is 0 or sh is 0:
            raise IndexSizeError()

        data = Uint8ClampedArray(sw * sh * 4)

        self._width = sw
        self._height = sh
        self._data = data

    @property
    def width(self):
        """
        A read-only reference to ImageData width property.
        """
        return self._width

    @property
    def height(self):
        """
        A read-only reference to ImageData height property.
        """
        return self._height

    @property
    def data(self):
        """
        A read-only reference to ImageData data property.
        """
        return self._data

