from pydantic import BaseModel


class VerifySignatureResponse(BaseModel):
    check: str