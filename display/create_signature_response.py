from pydantic import BaseModel

from display.curver import Signature


class CreateSignatureResponse(BaseModel):
    M: str
    signature: Signature