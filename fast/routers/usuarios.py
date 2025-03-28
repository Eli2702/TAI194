from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from modelsPydantic import modelUsuario
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter

#declarar objeto router
routerUsuario= APIRouter()

#ruta CONSULTA TODOS
@routerUsuario.get('/todosusuarios',tags=['Operaciones CRUD'])
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
@routerUsuario.get('/usuario/{id}', tags=['Operaciones CRUD'])
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
@routerUsuario.post('/usuarios/', response_model=modelUsuario, tags=['Operaciones CRUD'])
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
@routerUsuario.put('/usuarios/{id}', response_model=modelUsuario, tags=['Operaciones CRUD'])
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
@routerUsuario.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
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