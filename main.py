from fastapi import FastAPI
from app.routers import users, agenda, alimentos, clientes, logins, loginusers, uploads

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(agenda.router, prefix="/agenda", tags=["Agenda"])
app.include_router(alimentos.router, prefix="/alimentos", tags=["Alimentos"])
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(logins.router, prefix="/logins", tags=["Logins"])
app.include_router(loginusers.router, prefix="/loginusers", tags=["LoginUsers"])
app.include_router(uploads.router, prefix="/uploads", tags=["Uploads"])
