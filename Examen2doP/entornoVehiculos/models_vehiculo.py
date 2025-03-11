from pydantic import BaseModel,Field

class modelVehiculo(BaseModel):
    Año: int = Field(...,gt=0, description="Id siempre debe de ser positivo")
    Modelo: str = Field(..., min_length=4, max_length=25, description="Solo letras sin espacios min 1 max 25")
    Placa: str = Field(..., min_length=6, max_length=10, description="Solo letras sin espacios min 6 max 10")
    