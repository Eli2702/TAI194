from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from models import modelUsuario, modelAuth
from genToken import createToken
from middlewares import BearerJWT

app= FastAPI(
    title="Mi primer API",
    description="Alma Elizabeth Tapia León",
    version="1.0.0"
)



usuarios =[
    {"id":1, "nombre": "Eduardo", "edad": 21, "correo": "edu21@example.com"},
    {"id":2, "nombre": "Maria", "edad": 28, "correo": "mar28@example.com"},
    {"id":3, "nombre": "Jesus", "edad": 34,"correo": "jes34@example.com"},
    {"id":4, "nombre": "Ana", "edad": 25, "correo": "ana253@example.com"}
]


#ruta o EndPoint
@app.get('/', tags=['Inicio'])
def home():
    return {'Hello': 'worl fastApi'}

#EndPoint para generar Token
@app.post('/auth',tags=['Autentificacion'])
def auth(credenciales:modelAuth):
    if credenciales.mail == 'elileon27@example.com' and credenciales.passw == '123456789':
        token: str= createToken(credenciales.model_dump())
        print(token)
        return JSONResponse(content= token)
    else:
        return {"Aviso":"Usuario no cuenta con permiso"}


#ruta CONSULTA TODOS
@app.get('/todosusuarios',dependencies=[Depends(BearerJWT())], response_model= List[modelUsuario], tags=['Operaciones CRUD'])
def leer():
    return usuarios

#ruta POST
@app.post('/usuarios/', response_model=modelUsuario, tags=['Operaciones CRUD'])
def guardar(usuario:modelUsuario):
    for usr in usuarios:
        if usr["id"]== usuario.id:
            raise  HTTPException(status_code=400,detail="El usuario ya existe.")
    
    usuarios.append(usuario)
    return usuario

#ruta para actualizar
@app.put('/usuarios/{id}', response_model=modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:modelUsuario):
    for index,  usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400,detail="El usuario no existe.")

#ruta para eliminar
@app.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def eliminar(id:int):
    for index,  usr in enumerate(usuarios):
        if usr["id"] == id:
            return usuarios.pop(index)
    raise HTTPException(status_code=400,detail="El usuario no se puede borrar")