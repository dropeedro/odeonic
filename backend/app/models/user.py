# from pydantic import BaseModel, EmailStr
# from app.database import db  # Asegúrate de que la conexión a la base de datos esté bien configurada

# class UserCreate(BaseModel):
#     email: EmailStr
#     password: str | None = None  # Contraseña opcional para OAuth
#     oauth_provider: str | None = None
#     oauth_id: str | None = None

# class UserResponse(BaseModel):
#     id: str
#     email: EmailStr
#     roles: list[str] = ["user"]  # Asignar rol predeterminado

# from pydantic import BaseModel, EmailStr
# from app.database import db  # Asegúrate de que la conexión a la base de datos esté bien configurada
# from app.services.user_service import create_user, update_subscription, get_subscription_status


# class UserCreate(BaseModel):
#     email: EmailStr
#     password: str | None = None  # Contraseña opcional para OAuth
#     oauth_provider: str | None = None
#     oauth_id: str | None = None

# class UserResponse(BaseModel):
#     id: str
#     email: EmailStr
#     roles: list[str] = ["user"]  # Asignar rol predeterminado
#     subscription_id: str | None = None  # ID de la suscripción en Stripe
#     subscription_status: str | None = "inactive"  # Estado de la suscripción (active, canceled, etc.)
#     subscription_plan: str | None = None  # Plan al que el usuario está suscrito (personal, business, etc.)
#     subscription_renewal_date: str | None = None  # Fecha de renovación de la suscripción (opcional)

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
    subscription_id: str | None = None  # Stripe Subscription ID
    subscription_status: str | None = "inactive"  # active, canceled, etc.
    subscription_plan: str | None = None  # personal, business, etc.
    subscription_start_date: str | None = None  # Fecha de inicio de la suscripción
    subscription_end_date: str | None = None  # Fecha de finalización o renovación
    subscription_duration: int | None = 0  # Tiempo total suscrito (en días)

