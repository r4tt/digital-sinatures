from pydantic import BaseModel

from display.curver import Signature


class VerifySignatureRequest(BaseModel):
    userId: str
    M: str
    signature: Signature