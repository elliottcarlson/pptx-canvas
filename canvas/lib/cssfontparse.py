"""
============
CSSFontParse
============

A class to assist in parsing CSS short-hand font declarations as used in Canvas
font setting assignment.
"""
import re

class CSSFontParse(object):
    """
    Parse a CSS short-hand font declaration and break it out to the appropriate
    font declarations.
    """

    # http://stackoverflow.com/questions/10135697/regex-to-parse-any-css-font
    pattern = r'^\s*(?=(?:(?:[-a-z]+\s*){0,2}(italic|oblique))?)(?=(?:(?:[-a' +\
              r'-z]+\s*){0,2}(small-caps))?)(?=(?:(?:[-a-z]+\s*){0,2}(bold(?' +\
              r':er)?|lighter|[1-9]00))?)(?:(?:normal|\1|\2|\3)\s*){0,3}((?:' +\
              r'xx?-)?(?:small|large)|medium|smaller|larger|[.\d]+(?:\%|in|[' +\
              r'cem]m|ex|p[ctx]))(?:\s*\/\s*(normal|[.\d]+(?:\%|in|[cem]m|ex' +\
              r'|p[ctx])))?\s*([-,\"\sa-z]+?)\s*$'

    _fontStyle = 'normal'
    _fontVariant = 'normal'
    _fontWeight = 'normal'
    _fontSize = '10px'
    _lineHeight = 'normal'
    _fontFamily = 'sans-serif'

    def __init__(self, font=''):
        match = re.compile(self.pattern, re.I).match(font)
        if match:
            self._fontStyle = match.group(1) or self._fontStyle
            self._fontVariant = match.group(2) or self._fontVariant
            self._fontWeight = match.group(3) or self._fontWeight
            self._fontSize = match.group(4) or self._fontSize
            self._fontFamily = match.group(6) or self._fontFamily

    def __str__(self):
        components = []
        properties = [
            '_fontStyle', '_fontVariant', '_fontWeight',
            '_fontSize', '_fontFamily'
        ]

        for prop in properties:
            if getattr(self, prop) is not 'normal':
                components.append(getattr(self, prop))

        return ' '.join(components)

    @property
    def fontStyle(self):
        return self._fontStyle

    @property
    def fontVariant(self):
        return self._fontVariant

    @property
    def fontWeight(self):
        return self._fontWeight

    @property
    def fontSize(self):
        return self._fontSize

    @property
    def lineHeight(self):
        return self._lineHeight

    @property
    def fontFamily(self):
        return self._fontFamily
