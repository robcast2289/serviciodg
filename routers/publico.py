from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/publico",
    tags=["Publico"],
)

@router.get("/")
async def get():
    return { "Versión":"1.0.1" }