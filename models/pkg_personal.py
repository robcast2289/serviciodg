from repositories.oracle.ora_db import Oradb, ODBType, ODBFunctionType

class PkgPersonal:
    def DatosGenerales(Codpers:str):
        params = [
            {
                "nombre": "PUSUARIO",
                "tipo": ODBType.VARCHAR2,
                "valor": '',
                "direccion": "IN"
            },
            {
                "nombre": "PCODPERS",
                "tipo": ODBType.VARCHAR2,
                "valor": Codpers,
                "direccion": "IN"
            },
            {
                "nombre": "RETVAL",
                "valor": '',
                "tipo": ODBType.SYS_REFCURSOR,
                "direccion": "OUT"
            },
        ]
        ret = Oradb().execute_procedure("DBAFISICC.PKG_PERSONAL.DATOS_GENERALES",params)
        return ret["RETVAL"]