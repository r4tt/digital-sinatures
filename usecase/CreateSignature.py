import random

from tinyec.ec import Curve
from extension.EEA import eea
from model.PublicKey import PublicKey
from model.Signature import Signature


def createSignature(M, E: Curve, publicKey: PublicKey, d):
    r, s = 0, 0
    n = E.field.n
    while r == 0 or s == 0:
        k = random.randint(0, n)
        r = (publicKey.P * k).x % n
        k1 = eea(k, n)
        s = (k1 * (M + d * r)) % n
    return Signature(M, r, s)
