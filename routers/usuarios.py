from fastapi import APIRouter, Depends, Header, HTTPException, status
from typing import List, Annotated, Union
import hashlib
from schemas.UsuariosSchema import UsuariosRequest
from models.pkg_ci import PkgCI
from models.pkg_usuario import PkgUsuario

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
)

async def get_user(token: Annotated[Union[str, None], Header()] = None):
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN)
    
    return token

@router.post("/autenticar")
async def autenticar(model:UsuariosRequest, user:str = Depends(get_user)):

    if not model.Usuario == user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario es incorrecto.")

    Contrasena = hashlib.sha512(model.Contrasena.encode("utf-8"))
    Hash = str(Contrasena.hexdigest())

    Autenticado = PkgCI.AutenticarAdministrativo(model.Usuario, Hash)

    return bool(Autenticado)


@router.get('/vinculos')
async def vinculos(user:str = Depends(get_user)):
    ret = PkgUsuario.Linksdigitalizacion(user)
    return ret