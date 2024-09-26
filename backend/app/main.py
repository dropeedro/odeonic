from fastapi import FastAPI
from app.routers import users, plans, secure_data

app = FastAPI()

# Incluir las rutas
app.include_router(users.router)
app.include_router(plans.router)
app.include_router(secure_data.router)
