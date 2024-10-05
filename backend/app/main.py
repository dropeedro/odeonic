from fastapi import FastAPI
from app.routers import users, plans, secure_data
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.auth.keycloak import verify_token

app = FastAPI()

# Incluir las rutas
app.include_router(users.router)
app.include_router(plans.router)
app.include_router(secure_data.router)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Middleware para verificar el token en cada request protegido
async def keycloak_auth(token: str = Depends(oauth2_scheme)):
    try:
        payload = verify_token(token)
        return payload  # Retorna los datos del token si es válido
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Ejemplo de ruta protegida
@app.get("/protected")
async def protected_route(user_data: dict = Depends(keycloak_auth)):
    return {"message": "Welcome to a protected route!", "user": user_data}
