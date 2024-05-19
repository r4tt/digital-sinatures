from tinyec.ec import Curve

from extension.EEA import eea
from model.Signature import Signature


def verifySignature(E: Curve, i, d, signature: Signature):
    P = E.g * i
    Q = P * d
    n = E.field.n
    if signature.r not in range(0, n) or signature.s not in range(0, n):
        return False
    w = eea(signature.s, n)
    u1 = signature.M * w % n
    u2 = signature.r * w % n
    point = u1 * P + u2 * Q
    return point.x == signature.r
