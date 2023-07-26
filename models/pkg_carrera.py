from repositories.oracle.ora_db import Oradb, ODBType, ODBFunctionType

class PkgCarrera:
    def fuc():
        params = [
            {
                "nombre": "RETVAL",
                "valor": '',
                "tipo": ODBType.SYS_REFCURSOR,
                "direccion": "OUT"
            },
        ]
        ret = Oradb().execute_procedure("DBAFISICC.PKG_CATALOGO.CATIPOCONVENIOSTB",params)
        return ret["RETVAL"]