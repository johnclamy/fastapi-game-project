from pydantic import BaseModel


class Gem(BaseModel):
    name: str
    country_of_origin: str
    area_of_discovery: str
    color: str
    value: int
    description: str
