from fastapi import FastAPI, HTTPException


app= FastAPI(
    title="Miprimer API",
    description="Alma Elizabeth Tapia León",
    version="1.0.0"
)

tareas =[
    {"id":2, "Titulo": "Gestion", "Descripcion": "Exposicion", "Vencimiento": "14-02-2024 23:59", "Estado": "No completada"},
    {"id":3, "Titulo": "Ingles", "Descripcion": "Actividades Cambridge", "Vencimiento": "24-02_2024", "Estado": "No completada"},
    {"id":4, "Titulo": "Sistemas", "Descripcion": "Sistema inteligente de alumnos", "Vencimiento": "17-02-2024", "Estado": "Completada"},
    {"id":5, "Titulo": "Virtualizacion", "Descripcion": "Virtualizar en Docker", "Vencimiento": "17-02-2024", "Estado": "Completada"},
    {"id":6, "Titulo": "Administracion", "Descripcion": "Apuntes de la Pag. 10-15", "Vencimiento": "12-02-2024", "Estado": "Completada"}
]


#Buscar tarea por ID
@app.get('/tarea/{id}', tags=['Tareas'])
def buscar(id:int):
    for index,  tra in enumerate(tareas):
        if tra ["id"] == id:
            return tareas[index]
    raise HTTPException(status_code=400,detail="Tarea no encontrada")

#Todas las Tareas
@app.get('/tarea', tags=['Tareas'])
def leer():
    return {'Tareas Registradas' : tareas}


#Crear tarea
@app.post('/tarea', tags=['Tareas'])
def guardar(tarea:dict):
    for tra in tareas:
        if tra["id"]== tarea.get("id"):
            raise  HTTPException(status_code=400,detail="Esta tarea ya existe")
    
    tareas.append(tarea)
    return tarea

#Actualizar tarea
@app.put('/tarea/{id}', tags=['Tareas'])
def actualizar(id:int,tareaActualizada:dict):
    for index,  tra in enumerate(tareas):
        if tra ["id"] == id:
            tareas[index].update(tareaActualizada)
            return tareas[index]
    raise HTTPException(status_code=400,detail="Tarea no encontrada")

#Eliminar tarea
@app.delete('/tarea/{id}', tags=['Tareas'])
def eliminar(id:int):
    for index,  tra in enumerate(tareas):
        if tra["id"] == id:
            return tareas.pop(index)
    raise HTTPException(status_code=400,detail="Esta tarea no se puede borrar")

