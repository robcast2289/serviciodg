from fastapi import APIRouter, Depends, Query
from typing import Annotated, List, Optional
from schemas.EtiquetasSchema import EtiquetasRequest, Etiqueta
from models.pkg_digitalizacion import PkgDigitalizacion
from pydantic import BaseModel, ValidationError, Field
from fastapi.exceptions import RequestValidationError
from datetime import datetime
import inspect
import json


class QueryBaseModel(BaseModel):
    def __init_subclass__(cls, *args, **kwargs):
        #super().__init_subclass__(**kwargs)
        field_default = Query(...)
        new_params = []
        print(cls.__fields__)
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
            print(**data)
            try:
                print(cls(**data))
                return cls(**data)
            except ValidationError as e:
                raise RequestValidationError(repr(e.errors()[0]['type']))

        sig = inspect.signature(_as_query)
        sig = sig.replace(parameters=new_params)
        _as_query.__signature__ = sig  # type: ignore
        setattr(cls, "as_query", _as_query)

    @staticmethod
    def as_query(parameters=[]) -> "QueryBaseModel":
        print('parameters')
        raise NotImplementedError

class ParamModelDetail(QueryBaseModel):
    Etiqueta: str = Field(default=None, alias='Etiquteta', required=False)
    Valor: str = Field(default=None, alias='Valor', required=False)

class ParamModel(QueryBaseModel):
    Aplicacion: Optional[str] #= Field(default=None, alias='Aplicacion', required=False)
    Categoria: Optional[str] #= Field(default=None, alias='Categoria', required=False)
    #Etiquetas: List[ParamModelDetail] = Field(default=None, alias='Etiquetas', required=False)


router = APIRouter(
    prefix="/etiquetas",
    tags=["Etiquetas"],
)


@router.get("/")
async def etiquetas():
    ret = PkgDigitalizacion.Etiquetas()
    return ret


""" @router.get("/archivo")
async def archivo(model:EtiquetasRequest = Depends(EtiquetasRequest.as_query)):
    print(model.Aplicacion)
    return model """
@router.get("/archivo")
async def archivo(Aplicacion: str, Categoria: int, Etiquetas: str = Query(...)):
    etiquetas_list = json.loads(Etiquetas)
    etiquetas_obj = []
    for etiqueta in etiquetas_list:
        etiquetas_obj.append(Etiqueta(Etiqueta=etiqueta["Etiqueta"], Valor=etiqueta["Valor"]))

    params = EtiquetasRequest(Aplicacion=Aplicacion, Categoria=Categoria, Etiquetas=etiquetas_obj)
    return params.Etiquetas[0].Etiqueta



@router.get("/api")
def test(q_param: ParamModel = Depends(ParamModel.as_query)):
    #start_datetime = q_param.Nombre
    return q_param