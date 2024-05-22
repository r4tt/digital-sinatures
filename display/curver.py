from pydantic import BaseModel


class Signature(BaseModel):
    r: str
    s: str

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Curve:
    def __init__(self, a, b, p, r):
        self.a = a
        self.b = b
        self.p = p
        self.r = r
