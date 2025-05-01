from pydantic import BaseModel

class GoldInput(BaseModel):
    SPX: float
    USO: float
    SLV: float
    EUR_USD: float
