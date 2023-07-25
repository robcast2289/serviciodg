from pydantic import BaseModel

class UsuariosRequest(BaseModel):
    Usuario: str
    Contrasena: str