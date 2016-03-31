from uint8clampedarray import Uint8ClampedArray
from pprint import pprint


x = Uint8ClampedArray(3)
pprint(x)
pprint(x[0])

x[0] = -17
x[1] = 93
x[2] = 350

pprint(x[0])
pprint(x[1])
pprint(x[2])
pprint(len(x))

