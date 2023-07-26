from pydantic import BaseModel, conint

class Etiqueta(BaseModel):
    Etiqueta:int
    Valor: int

class EtiquetasRequest(BaseModel):
    Aplicacion:str
    Categoria:conint(ge=0)
    Etiquetas: list[Etiqueta]
