from display.create_key_response import PublicKey


class GetUserInfoResponse:
    def __init__(self, userId: str, publicKey: PublicKey):
        self.userId = userId
        self.publicKey = publicKey