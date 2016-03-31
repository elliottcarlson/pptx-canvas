"""
===============
CanvasImageData
===============
"""
class ImageData(object):

class CanvasImageData(object):
    """
    [NoInterfaceObject]
    interface CanvasImageData {
        // pixel manipulation
        ImageData createImageData(double sw, double sh);
        ImageData createImageData(ImageData imagedata);
        ImageData getImageData(double sx, double sy, double sw, double sh);
        void putImageData(ImageData imagedata, double dx, double dy);
        void putImageData(ImageData imagedata, double dx, double dy, double dirtyX, double dirtyY, double dirtyWidth, double dirtyHeight);
    };
    """

    def __init__(self):
        if type(self) == CanvasImageData:
            raise Exception('<CanvasImageData> must be subclassed.')

    def createImageData(self, sw, sh):
        """
        Returns an ImageData object with the given dimensions. All the pixels in
        the returned object are transparent black.

        Throws an IndexSizeError exception if either of the width or height
        arguments are zero.
        """
        return ImageData(sw, sh)
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
