from pydantic import BaseModel
from .EtiquetasSchema import EtiquetasRequest as EtiquetasImportRequest

class ArchivosRequest(BaseModel):
    ID:int


class ArchivoResult(BaseModel):
    Ruta:str
    Nombre:str
    Extension:str
    Extencionfisica:str


class EtiquetasRequest(BaseModel):
    IDArchivo:int


class ArchivosPostRequest(EtiquetasImportRequest):
    Agregar:bool

