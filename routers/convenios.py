from fastapi import APIRouter
from models.pkg_catalogo import PkgCatalogo

router = APIRouter(
    prefix="/convenios",
    tags=["Convenios"],
)

@router.get("/")
async def convenios():
    ret = PkgCatalogo.TipoConvenio()
    return ret