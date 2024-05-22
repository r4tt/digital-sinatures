from pydantic import BaseModel


class Signature(BaseModel):
    r: str
    s: str

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Curve(BaseModel):
    a: int
    b: int
    p: int
    r: int
