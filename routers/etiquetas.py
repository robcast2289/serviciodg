from fastapi import APIRouter, Query
from schemas.EtiquetasSchema import EtiquetasRequest, Etiqueta
from models.pkg_digitalizacion import PkgDigitalizacion
import json
import pandas as pd


def Archivos(model: EtiquetasRequest):
    IDArchivos = []

    for etiqueta in model.Etiquetas:
        archivos = PkgDigitalizacion().Idarchivo(model.Aplicacion,model.Categoria,etiqueta.Etiqueta,etiqueta.Valor)
        IDArchivos.append(archivos)

    # Transforma la lista de listas en una sola lista
    IDArchivos_flat = [item for sublist in IDArchivos for item in sublist]
    # Convertir las listas en DataFrames
    df_archivos = pd.DataFrame(IDArchivos_flat, columns=['IDArchivo'])
    # Realizar el agrupamiento y filtro
    resultados = df_archivos.groupby('IDArchivo').filter(lambda x: x['IDArchivo'].count() == len(model.Etiquetas))
    # Obtener los valores agrupados que cumplen con la condición
    valores_finales = resultados['IDArchivo'].unique().tolist()

    return valores_finales


router = APIRouter(
    prefix="/etiquetas",
    tags=["Etiquetas"],
)


@router.get("/")
async def etiquetas():
    ret = PkgDigitalizacion().Etiquetas()
    return ret


@router.get("/archivo/")
async def archivo(Aplicacion: str, Categoria: int, Etiquetas: str = Query(...)):
    etiquetas_list = json.loads(Etiquetas)
    etiquetas_obj = []
    for etiqueta in etiquetas_list:
        etiquetas_obj.append(Etiqueta(Etiqueta=etiqueta["Etiqueta"], Valor=etiqueta["Valor"]))

    params = EtiquetasRequest(Aplicacion=Aplicacion, Categoria=Categoria, Etiquetas=etiquetas_obj)

    ret = Archivos(params)
    return int(ret[0])


@router.get("/archivos")
async def archivos(Aplicacion: str, Categoria: int, Etiquetas: str = Query(...)):
    etiquetas_list = json.loads(Etiquetas)
    etiquetas_obj = []
    for etiqueta in etiquetas_list:
        etiquetas_obj.append(Etiqueta(Etiqueta=etiqueta["Etiqueta"], Valor=etiqueta["Valor"]))

    params = EtiquetasRequest(Aplicacion=Aplicacion, Categoria=Categoria, Etiquetas=etiquetas_obj)

    ret = Archivos(params)

    lst = list()
    for IDArchivo in ret:
        lst.append(PkgDigitalizacion().Archivovalido(IDArchivo)[0])

    return lst
