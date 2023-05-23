import random

from tinyec.ec import Curve

from model.PublicKey import PublicKey

def createKey(E: Curve):
    i = random.randint(0, E.field.n)
    P = E.g * i
    d = random.randint(0, E.field.n)
    Q = P * d
    return d, PublicKey(E, P, E.field.n, Q)
