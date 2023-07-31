from fastapi import APIRouter, Query, Depends
from typing import List
from models.pkg_carrera import PkgCarrera
from models.pkg_digitalizacion import PkgDigitalizacion
from schemas.CarrerasSchema import CarrerasRequest,TitulosRequest, CarrerasCarrerasRequest, CarrerasCarrerasResponse

router = APIRouter(
    prefix="/carreras",
    tags=["Carreras"],
)

@router.get("/{ID}")
async def carreras(ID:str):
    ret = PkgDigitalizacion().Obtenercarrerasxcarnet(ID)
    return ret


@router.get("/entidad/")
async def entidad(model:CarrerasRequest = Depends()):
    ret = PkgDigitalizacion().Entidad(model.Carrera)
    return ret


@router.get("/titulos/")
async def titulos(model:TitulosRequest = Depends()):
    ret = PkgDigitalizacion().Obtenertitulosxcarrera(model.Carrera,model.Titulo)
    return ret


@router.get("/nombrecarreras/")
async def titulos(model:CarrerasCarrerasRequest = Depends()):
    ret = PkgDigitalizacion().Nombrecarreras(model.BuscarCarrera)

    lst = list()
    for carrera in ret:
        carr = CarrerasCarrerasResponse()
        carr.Carrera = carrera["Carrera"]
        carr.Nombre = carrera["Nombre_Completo_2"]
        lst.append(carr)
    return lst