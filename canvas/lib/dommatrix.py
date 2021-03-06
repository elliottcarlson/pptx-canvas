"""
=================
DOMMatrixReadOnly
=================
"""
from .dommatrixreadonly import DOMMatrixReadOnly
import re

class DOMMatrix(DOMMatrixReadOnly):

    def __init__(self, *args, **kwargs):
        super(DOMMatrix, self).__init__(*args, **kwargs)

    def __setattr__(self, key, value):
        match = re.search(r'^m[1-4][1-4]$', key)
        if match and key in self._matrix:
            self._matrix[key] = value
        elif key in self.__dict__:
            self.__dict__[key] = value
        else:
            raise AttributeError('can\'t set attribute')

