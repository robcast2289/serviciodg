from fastapi import APIRouter
from models.pkg_encabezado import PkgEncabezado

router = APIRouter(
    prefix="/facultades",
    tags=["Facultades"],
)


@router.get('/')
async def facultades():
    ret = PkgEncabezado.Facultad('',"002",1,0,0)
    return ret