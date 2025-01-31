from fastapi import FastAPI
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


#EndPoint Promedio
@app.get('/promedio', tags=['Mi calificacion TAI'])
def promedio():
    return 10.5

#EndPoint con parametro obligatorio
@app.get('/usuario/{id}', tags=['EndPoint Parametro obligatorio'])
def consultausuario(id:int):
    #caso ficticio de busqueda en BD
    return {"Se encontro el usuario":id}


#EndPoint con parametro opcional
@app.get('/usuario2/', tags=['EndPoint Parametro opcional'])
def consultausuario2(id: Optional[int]=None):
    if id is not None:
        for usuario in usuarios:   #usuario llave para las iteraciones, ususarios lista
            if usuario ["id"] == id:
                return {"mensaje": "usuario encontrado", "El usuario es:": usuario}
        return {"mensaje": f"No se encontro el Id: {id}"}
    
    return {"mensaje":"No se proporciono un Id"}


#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}