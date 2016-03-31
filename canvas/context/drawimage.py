"""
===============
CanvasDrawImage
===============
"""
class CanvasDrawImage(object):
    """
    [NoInterfaceObject]
    interface CanvasDrawImage {
        // drawing images
        void drawImage(CanvasImageSource image, unrestricted double dx,
            unrestricted double dy);
        void drawImage(CanvasImageSource image, unrestricted double dx,
            unrestricted double dy, unrestricted double dw, unrestricted double dh);
        void drawImage(CanvasImageSource image, unrestricted double sx,
            unrestricted double sy, unrestricted double sw, unrestricted double
            sh, unrestricted double dx, unrestricted double dy, unrestricted
            double dw, unrestricted double dh);
    };
    """

    def __init__(self):
        if type(self) == CanvasDrawImage:
            raise Exception('<CanvasDrawImage> must be subclassed.')

    def drawImage(self, image, sx=0, sy=0, sw=None, sh=None, dx=0, dy=0,
            dw=None, dh=None):
        """
        Draws the given image onto the canvas. The arguments are interpreted as
        follows:

        https://html.spec.whatwg.org/images/drawImage.png

        If the image isn't yet fully decoded, then nothing is drawn. If the
        image is a canvas with no data, throws an InvalidStateError exception.
        """
        pass
