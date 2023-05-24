from tinyec.ec import Curve

from extension.EEA import eea
from model.PublicKey import PublicKey
from model.Signature import Signature


def verifySignature(E: Curve, publicKey: PublicKey, signature: Signature):
    n = E.field.n
    if signature.r not in range(0, n) or signature.s not in range(0, n):
        return False
    w = eea(signature.s, n)
    u1 = signature.M * w % n
    u2 = signature.r * w % n
    point = u1 * publicKey.P + u2 * publicKey.Q
    return point.x == signature.r
