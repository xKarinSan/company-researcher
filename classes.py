from pydantic import BaseModel
from datetime import datetime

class Price(BaseModel):
    pricing_type: str
    price_amount: float
    
class Competitor(BaseModel):
    name: str
    market_share: float
    pricing:list[Price]
    advantages:list[str]
    disadvantages:list[str]
        
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
    competitors: list[Competitor]
    
