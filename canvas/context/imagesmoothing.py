"""
====================
CanvasImageSmoothing
====================

Objects that implement the CanvasImageSmoothing interface have attributes that
control how image smoothing is performed.
"""
class CanvasImageSmoothing(object):
    """
    [NoInterfaceObject]
    interface CanvasImageSmoothing {
        // image smoothing
        attribute boolean imageSmoothingEnabled; // (default true)
        attribute ImageSmoothingQuality imageSmoothingQuality; // (default low)
    };
    """
    _imageSmoothingEnabled = True
    _imageSmoothingQuality = 'low'

    def __init__(self):
        if type(self) == CanvasImageSmoothing:
            raise Exception('<CanvasImageSmoothing> must be subclassed.')

    @property
    def imageSmoothingEnabled(self):
        """
        Returns whether pattern fills and the drawImage() method will attempt to
        smooth images if their pixels don't line up exactly with the display,
        when scaling images up.
        """
        return self._imageSmoothingEnabled

    @imageSmoothingEnabled.setter
    def imageSmoothingEnabled(self, val):
        """
        Can be set, to change whether images are smoothed (true) or not (false).
        """
        self._imageSmoothingEnabled = bool(val)

    @property
    def imageSmoothingQuality(self):
        """
        Returns the current image-smoothing-quality preference.
        """
        return self._imageSmoothingQuality

    @imageSmoothingQuality.setter
    def imageSmoothingQuality(self, val):
        """
        Can be set, to change the preferred quality of image smoothing. Unknown
        values are ignored.
        """
        if val in ['low', 'medium', 'high']:
            self._imageSmoothingQuality = val

