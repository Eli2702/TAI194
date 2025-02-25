from pydantic import BaseModel,Field


class modelUsuario(BaseModel):
    id: int = Field(...,gt=0, description="Id siempre debe de ser positivo")
    nombre: str = Field(..., min_length=1, max_length=85, description="Solo letras y espacios min 1 max 85")
    edad: int = Field(..., gt=1, le=120, description="Edad siempre debe de ser positivo" )
    correo: str = Field (..., pattern = ("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"), example = ("edu21@example.com"))