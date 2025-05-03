from pydantic import BaseModel
from datetime import datetime
class GeneralInfo(BaseModel):
    name: str
    location: str
    founding_date: datetime
    mission: str
    values: list[str]
    products: list[str]
    industry: str
    market_segment: str
    business_model:str
    