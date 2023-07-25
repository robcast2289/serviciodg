from fastapi import APIRouter, HTTPException, status
from models.dynamics import Dynamics

router = APIRouter(
    prefix="/empleados",
    tags=["Empleados"],
)

@router.get("/{id}")
async def nombre(id:str):
    ret = Dynamics.ObtenerNombre(id)
    if not ret:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="El empleado no ha sido encontrado")
    return ret
