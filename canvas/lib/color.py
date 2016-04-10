from colour import Color as ColorBase
import re

class Color:

    colour = None

    def __init__(self, *args, **kwargs):
        self.colour = ColorBase(*args, **kwargs)

    def __getattr__(self, attr):
        return self.colour.__getattr__(attr)

    @property
    def hex(self):
        color = re.sub('^#', '', self.colour.__getattr__('hex_l'))
        return color

    def __str__(self):
        return "%s" % self.colour.__getattr__('web')

    def __repr__(self):
        return "<Color %s>" % self.colour.__getattr__('web')

