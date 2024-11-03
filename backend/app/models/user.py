from pydantic import BaseModel, EmailStr
from app.database import db  # Asegúrate de que la conexión a la base de datos esté bien configurada

class UserCreate(BaseModel):
    email: EmailStr
    password: str | None = None  # Contraseña opcional para OAuth
    oauth_provider: str | None = None
    oauth_id: str | None = None

class UserResponse(BaseModel):
    id: str
    email: EmailStr
    roles: list[str] = ["user"]  # Asignar rol predeterminado
