# from fastapi import FastAPI
# from app.routers import users, plans, secure_data
# from fastapi import FastAPI, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from app.auth.keycloak import verify_token

# app = FastAPI()

# # Incluir las rutas
# app.include_router(users.router)
# app.include_router(plans.router)
# app.include_router(secure_data.router)


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # Middleware para verificar el token en cada request protegido
# async def keycloak_auth(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = verify_token(token)
#         return payload  # Retorna los datos del token si es válido
#     except ValueError as e:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid or expired token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

# # Ejemplo de ruta protegida
# @app.get("/protected")
# async def protected_route(user_data: dict = Depends(keycloak_auth)):
#     return {"message": "Welcome to a protected route!", "user": user_data}

# from fastapi import FastAPI, HTTPException, Depends
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.security import OAuth2PasswordBearer
# from app.models.user import UserCreate, UserResponse, create_user
# from app.routers import users, plans, secure_data
# from app.auth.keycloak import verify_token
# from .keycloak_routes import router as keycloak_router

# app = FastAPI()

# # Configuración de CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],  # Cambia esto si tu frontend se sirve desde otro origen
#     allow_credentials=True,
#     allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
#     allow_headers=["*"],  # Permite todos los encabezados
# )

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # Middleware para verificar el token en cada request protegido
# async def keycloak_auth(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = verify_token(token)
#         return payload  # Retorna los datos del token si es válido
#     except ValueError:
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid or expired token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.post("/users", response_model=UserResponse)
# async def register_user(user: UserCreate):
#     # Lógica de registro de usuario
#     try:
#         return create_user(user)  # Llama a la función que inserta el usuario
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))  # Manejo de errores

# # Ejemplo de ruta protegida
# @app.get("/protected")
# async def protected_route(user_data: dict = Depends(keycloak_auth)):
#     return {"message": "Welcome to a protected route!", "user": user_data}

# # Incluir las rutas
# app.include_router(users.router)
# app.include_router(plans.router)
# app.include_router(secure_data.router)

# # Montar el router de Keycloak
# app.include_router(keycloak_router, prefix="/keycloak")

# from fastapi import FastAPI, Depends
# from fastapi.security import OAuth2PasswordRequestForm

# app = FastAPI()

# @app.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     # Aquí iría tu lógica de autenticación
#     return {"access_token": "token", "token_type": "bearer"}


from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr
from pymongo import MongoClient
import bcrypt
from app.routers import users, plans, secure_data
from app.auth.keycloak import verify_token
from app.keycloak_routes import router as keycloak_router

app = FastAPI()

app.include_router(keycloak_router)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Cambia esto según tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OAuth2 configuración
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Middleware para verificar el token
async def keycloak_auth(token: str = Depends(oauth2_scheme)):
    try:
        payload = verify_token(token)
        return payload
    except ValueError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Conexión a MongoDB
MONGODB_URI = "mongodb+srv://pedro:1234@cluster0.n22vyn8.mongodb.net/odeonic_test?retryWrites=true&w=majority"
client = MongoClient(MONGODB_URI)

try:
    db = client['odeonic_test']
    print("Conexión exitosa a MongoDB")
except Exception as e:
    print(f"Error conectando a MongoDB: {e}")

# Modelos Pydantic para validación de entrada y salida

class UserCreate(BaseModel):
    email: EmailStr
    password: str | None = None  # Contraseña opcional para OAuth
    oauth_provider: str | None = None
    oauth_id: str | None = None

class UserResponse(BaseModel):
    id: str
    email: EmailStr
    roles: list[str] = ["user"]  # Asignar rol predeterminado

# Función para hashear la contraseña
def hash_password(password: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

# Función para registrar un nuevo usuario
def create_user(user: UserCreate):
    user_data = user.dict()

    # Si el usuario se registra con formulario (sin OAuth), debe tener una contraseña
    if user.password:
        user_data["password"] = hash_password(user.password)
    else:
        # Si es un registro OAuth, no hasheamos la contraseña
        user_data["password"] = None

    # Inserta el nuevo usuario en la colección 'users'
    result = db.users.insert_one(user_data)
    return UserResponse(id=str(result.inserted_id), email=user.email)

# Ruta para registrar usuarios (con o sin OAuth)
@app.post("/register", response_model=UserResponse)
def register(user: UserCreate):
    existing_user = db.users.find_one({"email": user.email})
    
    if existing_user:
        raise HTTPException(status_code=400, detail="User already registered")
    
    new_user = create_user(user)
    return new_user

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Rutas protegidas con autenticación
@app.get("/protected")
async def protected_route(user_data: dict = Depends(keycloak_auth)):
    return {"message": "Welcome to a protected route!", "user": user_data}

# Incluyendo routers
app.include_router(users.router)
app.include_router(plans.router)
app.include_router(secure_data.router)
app.include_router(keycloak_router, prefix="/keycloak")

# Ruta de token
@app.post("/token")
async def login(form_data: OAuth2PasswordBearer = Depends()):
    return {"access_token": "token", "token_type": "bearer"}

@app.post("/test-insert-user")
def test_insert_user():
    user_data = {
        "email": "testoauthuser@example.com",
        "password": hash_password("password123"),  # Hashea la contraseña
        "oauth_provider": "google",  # Usuario creado vía OAuth
        "oauth_id": "google-oauth-id-123"
    }

    try:
        result = db.users.insert_one(user_data)  # Inserta el usuario en MongoDB
        return {"message": f"Usuario insertado con ID: {result.inserted_id}"}
    except Exception as e:
        return {"error": str(e)}

