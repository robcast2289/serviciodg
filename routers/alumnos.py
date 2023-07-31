from fastapi import APIRouter, Depends
from models.pkg_digitalizacion import PkgDigitalizacion
from models.pkg_academico import PkgAcademico
from models.pkg_alumno import PkgAlumno
from schemas.AlumnosSchema import AlumnosRequest, SolicitudesRequest

router = APIRouter(
    prefix="/alumnos",
    tags=["Alumnos"],
)

@router.get("/")
async def alumnos(model:AlumnosRequest = Depends()):
    ret = PkgDigitalizacion().Obtenernombrealumno(model.ID)[0]
    return ret


@router.get("/requisitosadmision")
async def alumnos():
    ret = PkgAcademico.RequisitosAdmision()
    return ret


@router.get("/solicitudespendientes/")
async def alumnos(model:SolicitudesRequest = Depends()):
    ret = PkgAlumno.TramitesSinTerminar(model.ID,model.Tramite,model.Carrera,model.Paso)
    return ret