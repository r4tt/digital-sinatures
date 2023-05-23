import random

from tinyec.ec import Curve
from extension.EEA import eea

def creatSignature(M, E: Curve, d):
    r, s = 0, 0
    n = E.field.n
    while r == 0 or s == 0:
        k = random.randint(0, n)
        r = (E.g * k).x % n
        k1 = eea(k , n)
        s = (k1 * M + d * r) % n
    return r, s