from typing import List
from pydantic import BaseModel, Field, ValidationError, conlist, conint
from fastapi import Query
from dataclasses import dataclass

from fastapi.exceptions import RequestValidationError
from datetime import datetime
import inspect

class QueryBaseModel(BaseModel):
    def __init_subclass__(cls, *args, **kwargs):
        field_default = Query(...)
        new_params = []
        for field in cls.__fields__.values():
            default = Query(field.default) if not field.required else field_default
            annotation = inspect.Parameter.empty

            new_params.append(
                inspect.Parameter(
                    field.alias,
                    inspect.Parameter.POSITIONAL_ONLY,
                    default=default,
                    annotation=annotation,
                )
            )

        async def _as_query(**data):
            try:
                return cls(**data)
            except ValidationError as e:
                raise RequestValidationError(repr(e.errors()[0]['type']))

        sig = inspect.signature(_as_query)
        sig = sig.replace(parameters=new_params)
        _as_query.__signature__ = sig  # type: ignore
        setattr(cls, "as_query", _as_query)

    @staticmethod
    def as_query(parameters: list) -> "QueryBaseModel":
        raise NotImplementedError

class Etiqueta(BaseModel):
    Etiqueta:int
    Valor: int
""" class Etiqueta:
    def __init__(self, Etiqueta: int, Valor: int):
        self.Etiqueta = Etiqueta
        self.Valor = Valor """

#@dataclass
class EtiquetasRequest(BaseModel):
    Aplicacion:str
    Categoria:conint(ge=0)
    Etiquetas: list[Etiqueta]
