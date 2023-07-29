from fastapi import Header, HTTPException, status
from typing import Annotated, Union

class UsuarioUtil:
    async def get_user(token: Annotated[Union[str, None], Header()] = None):
        if not token:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN)
        
        return token