from typing import List
from pydantic import BaseModel, Field
from fastapi import Query
from dataclasses import dataclass


class Etiqueta(BaseModel):
    Etiqueta:int
    Valor: str

#@dataclass
class EtiquetasRequest(BaseModel):
    Aplicacion:str
    Categoria:str
    Etiquetas: List[Etiqueta] = Field(Query(...,description="Some three comment"))
