from pydantic import BaseModel

class PlanCreate(BaseModel):
    name: str
    description: str
    price: float

class PlanResponse(PlanCreate):
    id: str

    class Config:
        orm_mode = True
