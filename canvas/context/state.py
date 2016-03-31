"""
===========
CanvasState
===========

When we draw on the Canvas context, we can make use of a stack of so-called
drawing states. Each of these states stores data about the Canvas context at any
one time. Here is a list of the data stored in the stack for each state:

    * Transformation matrix information such as rotations or translations using
      the context.rotate() and context.setTransform() methods
    * The current clipping region
    * The current values for canvas attributes, such as (but not limited to):
        - globalAlpha
        - globalCompositeOperation
        - strokeStyle
        - textAlign, textBaseline
        - lineCap, lineJoin, lineWidth, miterLimit
        - fillStyle
        - font
        - shadowBlur, shadowColor, shadowOffsetX, and shadowOffsetY

The current path and current bitmap being manipulated on the Canvas context are
not part of the saved state.

To save (push) the current state to the stack, call:
    context.save()

To restore the canvas by "popping" the last state saved to the stack, use:
    context.restore()
"""
class CanvasState(object):
    """
    [NoInterfaceObject]
    interface CanvasState {
        // state
        void save(); // push state on state stack
        void restore(); // pop state stack and restore state
    };
    """

    def __init__(self):
        if type(self) == CanvasState:
            raise Exception('<CanvasState> must be subclassed.')

    def save(self):
        """
        Push state on state stack.
        """
        pass

    def restore(self):
        """
        Pop state and restore state.
        """
        pass
