from fastapi import FastAPI, HTTPException
from models_vehiculo import modelVehiculo

app= FastAPI(
    title="Mi Examen",
    description="Alma Elizabeth Tapia León",
    version="1.0.0"
)

vehiculos =[
    {"Modelo":"Aveo", "Año": 2005, "Placa": "ADRT"},
    {"Modelo":"Nissan", "Año": 2012, "Placa": "ADER4"},
    {"Modelo":"Toyota", "Año": 2004, "Placa": "ADE3"},
    {"Modelo":"BMW", "Año": 2020, "Placa": "ADGTE"}
]

#LEER TODOS VEHICULOS
@app.get('/vehiculos', tags=['Operacion CRUD'])
def leer():
    return {'Vehiculos Registrados' : vehiculos}

#Guardar
@app.post('/vehiculos/', response_model=modelVehiculo, tags=['Operaciones CRUD'])
def guardar(vehiculo:modelVehiculo):
    for vhi in vehiculos:
        if vhi["Placa"]== vehiculo.Placa:
            raise  HTTPException(status_code=400,detail="El vehiculo ya existe.")
    
    vehiculos.append(vehiculo)
    return vehiculo

#Buscar por placa
@app.get('/vehiculos/{Placa}', tags=['Operaciones CRUD'])
def buscar(Placa:str):
    for index,  vhi in enumerate(vehiculos):
        if vhi ["Placa"] == Placa:
            return vehiculos[index]
    raise HTTPException(status_code=400,detail="Vehiculo no encontrado")