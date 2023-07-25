from fastapi import APIRouter, Depends, Query
from typing import Annotated
from schemas.EtiquetasSchema import EtiquetasRequest
from models.pkg_digitalizacion import PkgDigitalizacion

router = APIRouter(
    prefix="/etiquetas",
    tags=["Etiquetas"],
)

@router.get("/")
async def etiquetas():
    ret = PkgDigitalizacion.Etiquetas()
    return ret


@router.get("/archivo")
async def archivo(model:EtiquetasRequest = Query(...)):
    print(model.Aplicacion)
    return model