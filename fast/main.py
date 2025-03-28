from fastapi import FastAPI, HTTPException, Depends
from DB.conexion import engine, Base
from routers.usuarios import routerUsuario
from routers.auth import routerAuth

app= FastAPI(
    title="Mi primer API",
    description="Alma Elizabeth Tapia León",
    version="1.0.0"
)

Base.metadata.create_all(bind= engine)


#EndPoint Inicio
@app.get('/', tags=['Inicio'])
def home():
    return {'Hello': 'worl fastApi'}


app.include_router(routerUsuario)
app.include_router(routerAuth)


