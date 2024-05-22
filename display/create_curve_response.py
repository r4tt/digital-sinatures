from pydantic import BaseModel

from display.curver import Curve


class CreateCurveResponse(BaseModel):
    message: str
    curve: str
    point: str