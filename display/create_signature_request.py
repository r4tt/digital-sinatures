from pydantic import BaseModel


class CreateSignatureRequest(BaseModel):
    userId: str
    M: str