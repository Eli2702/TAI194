from fastapi import FastAPI


app= FastAPI()

tareas =[
    {"id":2, "Titulo": "Gestion", "Descripcion": "Exposicion", "Vencimiento": "14-02-2024 23:59", "Estado": "No completada"},
    {"id":3, "Titulo": "Ingles", "Descripcion": "Actividades Cambridge", "Vencimiento": "24-02_2024", "Estado": "No completada"},
    {"id":4, "Titulo": "Sistemas", "Descripcion": "Sistema inteligente de alumnos", "Vencimiento": "17-02-2024", "Estado": "Completada"},
    {"id":5, "Titulo": "Virtualizacion", "Descripcion": "Virtualizar en Docker", "Vencimiento": "17-02-2024", "Estado": "Completada"},
    {"id":6, "Titulo": "Administracion", "Descripcion": "Apuntes de la Pag. 10-15", "Vencimiento": "12-02-2024", "Estado": "Completada"}
]

@app.get('/')
def home():
    return {"id": 1,
            "titulo": "Estudiar para el examen",
            "descripcion": "Repasar los apuntes de TAI ",
            "vencimiento": "14-02-24",
            "Estado": "Completada"}

@app.get('/todasTareas', tags=['Operaciones CRUD'])
def leer():
    return {'Tareas Registradas' : tareas}

