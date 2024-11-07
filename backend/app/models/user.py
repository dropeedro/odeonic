from pydantic import BaseModel, Field

class Usuario(BaseModel):
    id: str | None = None
    email: str
    password: str
    oauth_provider: str | None = None
    oauth_id: str | None = None

    class Config:
        orm_mode = True
