from display.curver import Point
from model.PublicKey import PublicKey as DomainPublicKey


class PublicKey:
    def __init__(self, P, n, Q):
        self.P = P
        self.n = n
        self.Q = Q


class CreateKeyResponse:
    def __init__(self, publicKey, privateKey):
        self.publicKey = publicKey
        self.privateKey = privateKey


def getCreateKeyResponse(publicKey: DomainPublicKey, privateKey):
    return CreateKeyResponse(
        PublicKey(
            Point(
                publicKey.P.x,
                publicKey.P.y
            ),
            publicKey.n,
            Point(
                publicKey.Q.x,
                publicKey.Q.y
            ),
        ),
        privateKey
    )
