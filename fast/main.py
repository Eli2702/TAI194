from fastapi import FastAPI, HTTPException
from typing import Optional

app= FastAPI(
    title="Miprimer API",
    description="Alma Elizabeth Tapia León",
    version="1.0.0"
)

usuarios =[
    {"id":1, "nombre": "Eduardo", "edad": 21},
    {"id":2, "nombre": "Maria", "edad": 28},
    {"id":3, "nombre": "Jesus", "edad": 34},
    {"id":4, "nombre": "Ana", "edad": 25}
]


#ruta o EndPoint
@app.get('/', tags=['Inicio'])
def home():
    return {'Hello': 'worl fastApi'}

#ruta CONSULTA TODOS
@app.get('/todosusuarios', tags=['Operaciones CRUD'])
def leer():
    return {'Usuarios Registrados' : usuarios}

#ruta POST
@app.post('/', tags=['Operaciones CRUD'])
def guardar(usuario:dict):
    for usr in usuarios:
        if usr["id"]== usuario.get("id"):
            raise  HTTPException(status_code=400,detail="El usuario ya existe.")
    
    usuarios.append(usuario)
    return usuario

#ruta para actualizar
@app.put('/usuarios/{id}', tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:dict):
    for index,  usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    raise HTTPException(status_code=400,detail="El usuario no existe.")