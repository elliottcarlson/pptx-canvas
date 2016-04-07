"""
=================
DOMMatrixReadOnly
=================
"""
from dommatrixreadonly import DOMMatrixReadOnly
import re
from pprint import pprint

class DOMMatrix(DOMMatrixReadOnly):

    def __init__(self, *args):
        super(DOMMatrix, self).__init__(*args)

    def __setattr__(self, key, value):
        match = re.search(r'^m[1-4][1-4]$', key)
        if match and key in self._matrix:
            self._matrix[key] = value
        elif key in self.__dict__:
            self.__dict__[key] = value
        else:
            raise AttributeError('can\'t set attribute')

