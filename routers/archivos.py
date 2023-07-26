from fastapi import APIRouter, Depends
from models.pkg_digitalizacion import PkgDigitalizacion
from schemas.ArchivosSchema import ArchivosRequest

router = APIRouter(
    prefix="/archivos",
    tags=["Archivos"],
)

@router.get("/")
async def archivos(model:ArchivosRequest = Depends()):
    archivo = PkgDigitalizacion.Archivo(model.ID)[0]
    return archivo