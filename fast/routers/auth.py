from fastapi.responses import JSONResponse
from modelsPydantic import modelUsuario, modelAuth
from genToken import createToken
from fastapi import APIRouter

#declarar objeto router
routerAuth= APIRouter()

#EndPoint para generar Token
@routerAuth.post('/auth',tags=['Autentificacion'])
def auth(credenciales:modelAuth):
    if credenciales.mail == 'elileon27@example.com' and credenciales.passw == '123456789':
        token: str= createToken(credenciales.model_dump())
        print(token)
        return JSONResponse(content= token)
    else:
        return {"Aviso":"Usuario no cuenta con permiso"}