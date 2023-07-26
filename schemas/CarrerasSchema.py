from pydantic import BaseModel,Field

class CarrerasRequest(BaseModel):
    Carrera:str


class TitulosRequest(CarrerasRequest):
    Titulo:int


class CarrerasCarrerasRequest(BaseModel):
    BuscarCarrera:str

class CarrerasCarrerasResponse():
    Carrera:str
    Nombre:str