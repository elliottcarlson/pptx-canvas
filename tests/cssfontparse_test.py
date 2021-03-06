"""Tests for Canvas.CanvasRenderingContext2D.CSSFontParse"""

import unittest
from canvas.lib.cssfontparse import CSSFontParse

class CSSFontParseTest(unittest.TestCase):
    """Tests for CSSFontParse"""

    def test_case_1(self):
        f = CSSFontParse()
        self.assertEqual(f.fontStyle, 'normal')
        self.assertEqual(f.fontVariant, 'normal')
        self.assertEqual(f.fontWeight, 'normal')
        self.assertEqual(str(f.fontSize), "10")
        self.assertEqual(f.lineHeight, 'normal')
        self.assertEqual(f.fontFamily, 'sans-serif')

    def test_case_2(self):
        f = CSSFontParse('italic 10pt Courier')
        self.assertEqual(f.fontStyle, 'italic')
        self.assertEqual(f.fontVariant, 'normal')
        self.assertEqual(f.fontWeight, 'normal')
        self.assertEqual(str(f.fontSize), "10")
        self.assertEqual(f.lineHeight, 'normal')
        self.assertEqual(f.fontFamily, 'Courier')

    def test_case_3(self):
        f = CSSFontParse('bold italic small-caps 1em/1.5em verdana,sans-serif')
        self.assertEqual(f.fontStyle, 'italic')
        self.assertEqual(f.fontVariant, 'small-caps')
        self.assertEqual(f.fontWeight, 'bold')
        self.assertEqual(str(f.fontSize), "1")
        self.assertEqual(f.lineHeight, 'normal')
        self.assertEqual(f.fontFamily, 'verdana,sans-serif')

    def test_case_4(self):
        f = CSSFontParse('italic small-caps 800 1em/1.5em verdana,sans-serif')
        self.assertEqual(f.fontStyle, 'italic')
        self.assertEqual(f.fontVariant, 'small-caps')
        self.assertEqual(f.fontWeight, '800')
        self.assertEqual(str(f.fontSize), "1")
        self.assertEqual(f.lineHeight, 'normal')
        self.assertEqual(f.fontFamily, 'verdana,sans-serif')

    def test_case_5(self):
        f = CSSFontParse('random gibberish invalid font declaration')
        self.assertEqual(f.fontStyle, 'normal')
        self.assertEqual(f.fontVariant, 'normal')
        self.assertEqual(f.fontWeight, 'normal')
        self.assertEqual(str(f.fontSize), "10")
        self.assertEqual(f.lineHeight, 'normal')
        self.assertEqual(f.fontFamily, 'sans-serif')

    def test_case_6(self):
        f = CSSFontParse('bold italic small-caps 1em/1.5em verdana,sans-serif')
        self.assertEqual(str(f), 'italic small-caps bold 1 verdana,sans-serif')

if __name__ == "__main__" and __package__ is None:
    unittest.main()  # pragma: no cover

