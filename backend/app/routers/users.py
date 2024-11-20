from fastapi import APIRouter, HTTPException
from app.models.user import UserCreate, UserResponse
from app.db.user_crud import create_user, get_user_by_email
from app.services.user_service import create_user, update_subscription, get_subscription_status

router = APIRouter()

router = APIRouter()

@router.post("/users", response_model=UserResponse)
async def register_user(user: UserCreate):
    existing_user = get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    user_id = create_user(user.dict())
    return UserResponse(id=user_id, **user.dict())

@router.post("/users/")
async def create_user_endpoint(user_data: dict):
    """Endpoint para crear un nuevo usuario."""
    try:
        return create_user(user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/users/{email}/subscription")
async def update_subscription_endpoint(email: str, subscription_data: dict):
    """Endpoint para actualizar la suscripción de un usuario."""
    try:
        return update_subscription(
            email,
            subscription_id=subscription_data["subscription_id"],
            status=subscription_data["status"],
            plan=subscription_data["plan"],
            renewal_date=subscription_data.get("renewal_date")
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/users/{email}/subscription-status")
async def get_subscription_status_endpoint(email: str):
    """Endpoint para consultar el estado de la suscripción de un usuario."""
    try:
        return get_subscription_status(email)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
