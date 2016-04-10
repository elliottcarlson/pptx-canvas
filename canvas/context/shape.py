"""
PresentationML Shape Builder
"""
from lxml import etree, objectify
from lxml.builder import ElementMaker

class Shape(object):
    """
    Create a new Shape element in PresentationML
    """

    _nsmap = {
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    }

    _globals = {
        'shape': 0,
    }

    def __init__(self):
      self._a = ElementMaker(namespace=self._nsmap['a'], nsmap=self._nsmap)
      self._p = ElementMaker(namespace=self._nsmap['p'], nsmap=self._nsmap)
      self._r = ElementMaker(namespace=self._nsmap['r'], nsmap=self._nsmap)

      self._prstGeom = '<p:sp ' + self.xmlns('p', 'a') + ('>'
        '  <p:nvSpPr>'
        '    <p:cNvPr id="%s" name="%s"/>'
        '    <p:cNvSpPr/>'
        '    <p:nvPr/>'
        '  </p:nvSpPr>'
        '  <p:spPr>'
        '    <a:xfrm>'
        '      <a:off x="%s" y="%s"/>'
        '      <a:ext cx="%s" cy="%s"/>'
        '    </a:xfrm>'
        '    <a:prstGeom prst="%s">'
        '      <a:avLst/>'
        '    </a:prstGeom>'
        '  </p:spPr>'
        '</p:sp>'
      )

      self._custGeom = '<p:sp ' + self.xmlns('p', 'a') + ('>'
        '  <p:nvSpPr>'
        '    <p:cNvPr id="%s" name="%s"/>'
        '    <p:cNvSpPr/>'
        '    <p:nvPr/>'
        '  </p:nvSpPr>'
        '  <p:spPr>'
        '    <a:xfrm>'
        '      <a:off x="%s" y="%s"/>'
        '      <a:ext cx="%s" cy="%s"/>'
        '    </a:xfrm>'
        '    <a:custGeom>'
        '      <a:avLst/>'
        '      <a:gdLst/>'
        '      <a:ahLst/>'
        '      <a:cxnLst/>'
        '      <a:rect l="0" t="0" r="0" b="0"/>'
        '    </a:custGeom>'
        '  </p:spPr>'
        '</p:sp>'
      )

      self._cxnSp = '<p:cxnSp ' + self.xmlns('p', 'a') + ('>'
        '  <p:nvCxnSpPr>'
        '    <p.cNvPr id="%s" name="%s"/>'
        '    <p:cNvCxnSpPr/>'
        '    <p:nvPr/>'
        '  </p:nvCxnSpPr>'
        '  <p:spPr>'
        '    <a:xfrm>'
        '      <a:off x="%s" y="%s"/>'
        '      <a:ext cx="%s" cy="%s"/>'
        '    </a:xfrm>'
        '    <a:prstGeom prst="straightConnector1">'
        '      <a:avLst/>'
        '    </a:prstGeom>'
        '    <a:noFill/>'
        '  </p:spPr>'
        '</p:cxnSp>'
    )

    def xmlns(self, *prefixes):
        return ' '.join('xmlns:%s="%s"' % (p, self._nsmap[p]) for p in prefixes)

    def prstGeom(self, prst, x, y, w, h):
        """
        Return a new shape object. For example:

            shape('ellipse', x=0, y=0, w=971600, h=971600)

        Popular shapes include: 'line', 'rect', 'roundRect' and 'ellipse'.

        Refer <http://msdn.microsoft.com/en-us/library/documentformat.openxml.drawing.shapetypevalues(v=office.14).aspx>
        """
        id = self._globals['shape'] = self._globals['shape'] + 1
        shp = objectify.fromstring(self._prstGeom % (id, 'Shape %d' % id, x, y, w, h, prst))
        # setattr(shp, 'pr', shp.find('.//p:spPr', namespaces=nsmap))
        return shp

    def custGeom(self, x, y, w, h):
        id = self._globals['shape'] = self._globals['shape'] + 1
        shp = objectify.fromstring(self._custGeom % (id, 'Freeform %d' %id, x, y, w, h))
        return shp

    def color(self, schemeClr=None, srgbClr=None, prstClr=None, hslClr=None, sysClr=None, scrgbClr=None, **mod):
        """
        Return a new color object.
        You may use any one of the following ways of specifying colour:

            color(schemeClr='accent2')             # = second theme color
            color(prstClr='black')                 # = #000000
            color(hslClr=[14400000, 100.0, 50.0])  # = #000080
            color(sysClr='windowText')             # = window text color
            color(scrgbClr=(50000, 50000, 50000))  # = #808080
            color(srgbClr='aaccff')                # = #aaccff

        One or more of these modifiers may be specified:

        - alpha    : '10%' indicates 10% opacity
        - alphaMod : '10%' increased alpha by 10% (50% becomes 55%)
        - alphaOff : '10%' increases alpha by 10 points (50% becomes 60%)
        - blue     : '10%' sets the blue component to 10%
        - blueMod  : '10%' increases blue by 10% (50% becomes 55%)
        - blueOff  : '10%' increases blue by 10 points (50% becomes 60%)
        - comp     : True for opposite hue on the color wheel (e.g. red -> cyan)
        - gamma    : True for the sRGB gamma shift of the input color
        - gray     : True for the grayscale version of the color
        - green    : '10%' sets the green component to 10%
        - greenMod : '10%' increases green by 10% (50% becomes 55%)
        - greenOff : '10%' increases green by 10 points (50% becomes 60%)
        - hue      : '14400000' sets the hue component to 14400000
        - hueMod   : '600000' increases hue by 600000 (14400000 becomes 20000000)
        - hueOff   : '10%' increases hue by 10 points (50% becomes 60%)
        - inv      : True for the inverse color. R, G, B are all inverted
        - invGamma : True for the inverse sRGB gamma shift of the input color
        - lum      : '10%' sets the luminance component to 10%
        - lumMod   : '10%' increases luminance by 10% (50% becomes 55%)
        - lumOff   : '10%' increases luminance by 10 points (50% becomes 60%)
        - red      : '10%' sets the red component to 10%
        - redMod   : '10%' increases red by 10% (50% becomes 55%)
        - redOff   : '10%' increases red by 10 points (50% becomes 60%)
        - sat      : '100000' sets the saturation component to 100%
        - satMod   : '10%' increases saturation by 10% (50% becomes 55%)
        - satOff   : '10%' increases saturation by 10 points (50% becomes 60%)
        - shade    : '10%' is 10% of input color, 90% black
        - tint     : '10%' is 10% of input color, 90% white

        Refer <http://msdn.microsoft.com/en-in/library/documentformat.openxml.drawing(v=office.14).aspx>
        """
        ns = self.xmlns('a')
        if schemeClr:
            s = '<a:schemeClr %s val="%s"/>' % (ns, schemeClr)
        elif srgbClr:
            s = '<a:srgbClr %s val="%s"/>' % (ns, srgbClr)
        elif prstClr:
            s = '<a:prstClr %s val="%s"/>' % (ns, prstClr)
        elif hslClr:
            s = '<a:hslClr %s hue="%.0f" sat="%.2f%%" lum="%.2f%%"/>' % ((ns,) + tuple(hslClr))
        elif sysClr:
            s = '<a:sysClr %s val="%s"/>' % (ns, sysClr)
        elif scrgbClr:
            s = '<a:scrgbClr %s r="%.0f" g="%.0f" b="%.0f"/>' % ((ns,) + tuple(scrgbClr))
        color = objectify.fromstring(s)
        for arg, val in mod.items():
            if val is True:
                color.append(etree.fromstring('<a:%s %s/>' % (arg, ns)))
            else:
                color.append(etree.fromstring('<a:%s %s val="%s"/>' % (arg, ns, val)))
        return color
