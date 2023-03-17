import math

from DoubleThinLensCombination import DoubleThinLensCombination
from ThickLens import ThickLens

if __name__ == '__main__':
    s = DoubleThinLensCombination(50, 50, 10)
    print(s)

    lens1 = ThickLens(1,1,10,1.5)
    phi = lens1.phi()
    print(phi)

    d1 = lens1.d1()
    print(d1)



