from pydantic import BaseModel

class AlumnosRequest(BaseModel):
    ID:str


class SolicitudesRequest(AlumnosRequest):
    Carrera:str
    Tramite:int
    Paso:int