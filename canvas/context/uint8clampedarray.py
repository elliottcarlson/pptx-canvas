"""
=================
Uint8ClampedArray
=================

A view on to an ArrayBuffer that exposes it as an array of unsigned 8 bit
integers with clamped conversions
"""
from array import array

class Uint8ClampedArray(array):
    def __new__(cls, size=0):
        return array.__new__(cls, 'B', [0] * size)

    def __getitem__(self, key):
        return array.__getitem__(self, key)

    def __setitem__(self, key, value):
        if value < 0:
            value = 0
        elif value > 255:
            value = 255
        return array.__setitem__(self, key, value)

