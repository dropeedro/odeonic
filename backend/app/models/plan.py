from pydantic import BaseModel, Field

class Plan(BaseModel):
    id: str | None = None
    name: str
    price: float
    description: str

    class Config:
        orm_mode = True
