"""
==========
CanvasText
==========
"""
from .shape import Shape

class CanvasText(object):
    """
    [NoInterfaceObject]
    interface CanvasText {
        // text (see also the CanvasPathDrawingStyles and
        // CanvasTextDrawingStyles interfaces)
        void fillText(DOMString text, unrestricted double x, unrestricted double
            y, optional unrestricted double maxWidth);
        void strokeText(DOMString text, unrestricted double x, unrestricted
            double y, optional unrestricted double maxWidth);
        TextMetrics measureText(DOMString text);
    };
    """
    textCounter = 31337

    def __init__(self):
        if type(self) == CanvasText:
            raise Exception('<CanvasText> must be subclassed.')

    def fillText(self, text, x, y, maxWidth=None):
        """
        Fills the given text at the given position. If a maximum width is
        provided, the text will be scaled to fit that width if necessary.
        """
        pass

    def strokeText(self, text, x, y, maxWidth=None):
        """
        Strokes the given text at the given position. If a maximum width is
        provided, the text will be scaled to fit that width if necessary.
        """
        align = {
            'center': 'ctr',
            'start': 'l',
            'end': 'r',
            'left': 'l',
            'right': 'r'
        }

        bold = {
            "normal": "0",
            "bold": "1"
        }

        italic = {
            "normal": "0",
            "italic": "1"
        }

        text_id = self.textCounter + 1

        shapes = self._canvas._slide._element.find('.//p:spTree', namespaces=self.nsmap)
        shape = Shape()

        shapes.append(
            shape._p.sp(
                shape._p.nvSpPr(
                    shape._p.cNvPr(name='Shape %s' % str(text_id), id=str(text_id)),
                    shape._p.cNvSpPr(txBox='1'),
                    shape._p.nvPr()
                ),
                shape._p.spPr(
                    shape._a.xfrm(
                        shape._a.off(x=str(x), y=str(y)),
                        shape._a.ext(cx="1270000", cy="1270000")
                    ),
                    shape._a.prstGeom(
                        shape._a.avLst(),
                        prst="rect"
                    ),
                    shape._a.noFill(),
                    shape._a.ln(
                        shape._a.noFill()
                    )
                ),
                shape._p.txBody(
                    shape._a.bodyPr(
                        shape._a.noAutofit(),
                        anchorCtr="0", anchor="t", bIns="91425", lIns="91425",
                        rIns="91425", tIns="91425", wrap="none"
                    ),
                    shape._a.lstStyle(),
                    shape._a.p(
                        shape._a.pPr(
                            #shape._a.lnSpc(
                            #    shape._a.spcPct(val="11500"),
                            #),
                            shape._a.spcBef(
                                shape._a.spcPts(val="0")
                            ),
                            shape._a.spcAft(
                                shape._a.spcPts(val="0")
                            ),
                            shape._a.buClr(
                                shape._a.schemeClr(val="dk1")
                            ),
                            shape._a.buSzPct(val="25000"),
                            shape._a.buFont(typeface=self._font.fontFamily),
                            shape._a.buNone(),
                            indent="0", lvl="0", marL="0", marR="0", rtl="0",
                            algn=align[self.textAlign]
                        ),
                        shape._a.r(
                            shape._a.rPr(
                                shape._a.solidFill(
                                    shape._a.srgbClr(
                                        val=self.strokeStyle.hex
                                    )
                                ),
                                shape._a.latin(typeface=self._font.fontFamily),
                                shape._a.ea(typeface=self._font.fontFamily),
                                shape._a.cs(typeface=self._font.fontFamily),
                                shape._a.sym(typeface=self._font.fontFamily),
                                sz=str((int(self._font.fontSize) * 100)),
                                b=bold[self._font.fontWeight], lang="en",
                                i=italic[self._font.fontStyle], u="none",
                                cap="none", strike="noStrike"
                            ),
                            shape._a.t(str(text))
                        )
                    )
                )
            )
        )

        #txBody = shape.text(text, x, y, 1000, 1000) #self._canvas._slide_width, self._canvas._slide_height)
        #shapes.append(txBody)
        #pass

    def measureText(self, text):
        """
        Returns a TextMetrics object with the metrics of the given text in the
        current font.
        """
        pass
