import re
from starlette.routing import Route
from fastapi import FastAPI
from routers import publico, usuarios, empleados, facultades, etiquetas

app = FastAPI(
    version="1.0.1",
    title="Servicio DG Python",
)

# Agrega los Routers
app.include_router(publico.router)
app.include_router(usuarios.router)
app.include_router(empleados.router)
app.include_router(facultades.router)
app.include_router(etiquetas.router)


@app.get("/")
async def inicio():
    return "Hola mundo"


# Ignorar el case-sensitive
for route in app.router.routes:
    if isinstance(route, Route):
        route.path_regex = re.compile(route.path_regex.pattern, re.IGNORECASE)

# Agrega prefijo
app.mount("/v1/api",app)