from pydantic import BaseModel


class CreateKeyRequest(BaseModel):
    userId: str
