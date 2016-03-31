"""
===============
CanvasHitRegion
===============

Unsupported - this is a beta feature in Canvas, and does not translate to the
PPTX interface.
"""
class CanvasHitRegion(object):
    """
    [NoInterfaceObject]
    interface CanvasHitRegion {
        // hit regions
        void addHitRegion(optional HitRegionOptions options);
        void removeHitRegion(DOMString id);
        void clearHitRegions();
    };
    """

    def __init__(self):
        if type(self) == CanvasHitRegion:
            raise Exception('<CanvasHitRegion> must be subclassed.')

    def addHitRegion(self, options=None):
        """
        Adds a hit region to the bitmap.
        """
        raise Exception('Not implemented.')

    def remoteHitRegion(self, id):
        """
        Removes a hit region (and all its descendants) from the canvas bitmap.
        The argument is the ID of a region added using addHitRegion().

        The pixels that were covered by this region and its descendants are
        effectively cleared by this operation, leaving the regions
        non-interactive. In particular, regions that occupied the same pixels
        before the removed regions were added, overlapping them, do not resume
        their previous role.
        """
        raise Exception('Not implemented.')

    def clearHitRegions(self):
        """
        Removes all hit regions from the canvas bitmap.
        """
        raise Exception('Not implemented.')
