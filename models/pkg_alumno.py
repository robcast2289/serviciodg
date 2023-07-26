from repositories.oracle.ora_db import Oradb, ODBType, ODBFunctionType

class PkgAlumno:
    def TramitesSinTerminar(Carnet:str, Tramite:int, Carrera:str, Paso:int):
        params = [
            {
                "nombre": "PSQLCODE",
                "tipo": ODBType.NUMBER,
                "valor": '',
                "direccion": "OUT"
            },
            {
                "nombre": "PERROR",
                "tipo": ODBType.VARCHAR2,
                "valor": '',
                "direccion": "OUT"
            },
            {
                "nombre": "PRESP",
                "tipo": ODBType.NUMBER,
                "valor": '',
                "direccion": "OUT"
            },
            {
                "nombre": "RETVAL",
                "valor": '',
                "tipo": ODBType.SYS_REFCURSOR,
                "direccion": "OUT"
            },
            {
                "nombre": "PCARNET",
                "tipo": ODBType.VARCHAR2,
                "valor": Carnet,
                "direccion": "IN"
            },
            {
                "nombre": "PTRAMITE",
                "tipo": ODBType.INT,
                "valor": Tramite,
                "direccion": "IN"
            },
            {
                "nombre": "PCARRERA",
                "tipo": ODBType.VARCHAR2,
                "valor": Carrera,
                "direccion": "IN"
            },
            {
                "nombre": "PPASO",
                "tipo": ODBType.INT,
                "valor": Paso,
                "direccion": "IN"
            },
        ]
        ret = Oradb().execute_procedure("DBAFISICC.PKG_ALUMNO.TRAMITES_SINTERMINAR",params)
        retProc = ret["RETVAL"]
        lst = list()
        for solicitud in retProc:
            lst.append(solicitud["Solicitud"])
        return lst
    

    def StatusDb():
        params = []
        ret = Oradb().execute_function("DBAFISICC.PKG_ESTUDIANTES.STATUSDB",params,ODBFunctionType.NUMBER)
        return ret["RETORNO_FUNCION"]