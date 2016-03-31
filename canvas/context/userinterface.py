"""
===================
CanvasUserInterface
===================

Unsupported - this is a beta feature in Canvas, and does not translate to the
PPTX interface.
"""
class CanvasUserInterface(object):
    """
    [NoInterfaceObject]
    interface CanvasUserInterface {
        void drawFocusIfNeeded(Element element);
        void drawFocusIfNeeded(Path2D path, Element element);
        void scrollPathIntoView();
        void scrollPathIntoView(Path2D path);
    };
    """

    def __init__(self):
        if type(self) == CanvasUserInterface:
            raise Exception('<CanvasUserInterface> must be subclassed.')

    def drawFocusIfNeeded(self, void, path=None):
        """
        If the given element is focused, draws a focus ring around the current
        default path or the given path, following the platform conventions for
        focus rings.
        """
        if path is None:
            path = self._path
        raise Exception('Not implemented.')

    def scrollPathIntoView(self, path=None):
        """
        Scrolls the current default path or the given path into view. This is
        especially useful on devices with small screens, where the whole canvas
        might not be visible at once.
        """
        if path is None:
            path = self._path
        raise Exception('Not implemented.')
