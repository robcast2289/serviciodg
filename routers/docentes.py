from fastapi import APIRouter
from models.pkg_personal import PkgPersonal

router = APIRouter(
    prefix="/docentes",
    tags=["Docentes"],
)

@router.get("/{ID}")
async def nombre(ID:str):
    ret = PkgPersonal.DatosGenerales(ID)[0]
    return f"{ret['Nombre1']} {ret['Nombre2']} {ret['Apellido1']} {ret['Apellido2']}"