from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
from modelsPydantic import modelUsuario, modelAuth
from genToken import createToken
from DB.conexion import Session, engine, Base
from models.modelsDB import User
from middlewares import BearerJWT

app= FastAPI(
    title="Mi primer API",
    description="Alma Elizabeth Tapia León",
    version="1.0.0"
)

Base.metadata.create_all(bind= engine)



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
@app.get('/todosusuarios',tags=['Operaciones CRUD'])
def leer():
    db=Session()
    try:
        consulta= db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))

    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, 
                            content={"mesage": "No fue posible consultar", 
                                    "Error": str(e)})

    finally:
        db.close()


#Buscar por ID
@app.get('/usuario/{id}', tags=['Operaciones CRUD'])
def leeruno(id:int):
    db=Session()
    try:
        consulta1= db.query(User).filter(User.id == id).first()
        if not consulta1:
            return JSONResponse(status_code=404, content={"Mensaje": "Usuario no encontrado"})

        return JSONResponse(content=jsonable_encoder(consulta1))

    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, 
                            content={"mesage": "No fue posible consultar", 
                                    "Error": str(e)})

    finally:
        db.close()

    

#ruta POST
@app.post('/usuarios/', response_model=modelUsuario, tags=['Operaciones CRUD'])
def guardar(usuario:modelUsuario):
    db=Session()
    try:
        db.add(User(**usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, 
                            content={"mesage": "Usuario guardado", 
                                    "usuario": usuario.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, 
                            content={"mesage": "No fue posible guardar usuario ", 
                                    "Error": str(e)})

    finally:
        db.close()


#ruta para actualizar
@app.put('/usuarios/{id}', response_model=modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:modelUsuario):
    db=Session()
    try:
        consulta2= db.query(User).filter(User.id == id).first()
        if not consulta2:
            return JSONResponse(status_code=404, content={"Mensaje": "Usuario no encontrado"})
        
        for key, value in usuarioActualizado.model_dump().items():
            setattr(consulta2, key, value)

        db.commit()  # Confirmar cambios
        db.refresh(consulta2)

        return JSONResponse(content=jsonable_encoder(consulta2))
    
    except Exception as e:
         db.rollback()
         return JSONResponse(status_code=500, 
                            content={"mesage": "No fue posible actualizar usuario ", 
                                    "Error": str(e)})

    finally:
        db.close()

#ruta para eliminar
@app.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def eliminar(id:int):
    db=Session()
    try:
        consulta3= db.query(User).filter(User.id == id).first()
        if not consulta3:
            return JSONResponse(status_code=404, content={"Mensaje": "Usuario no eliminado"})
        db.delete(consulta3)  
        db.commit()

        return JSONResponse(content=jsonable_encoder(consulta3))

    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, 
                            content={"mesage": "No fue posible consultar", 
                                    "Error": str(e)})

    finally:
        db.close()