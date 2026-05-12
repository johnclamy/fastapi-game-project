from pydantic import BaseModel


class Explorer(BaseModel):
    name: str
    gender: str
    nationality: str
    age: int
    experience: int
    description: str
