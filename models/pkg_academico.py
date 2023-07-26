from repositories.oracle.ora_db import Oradb, ODBType, ODBFunctionType

class PkgAcademico:
    def RequisitosAdmision():
        params = [
            {
                "nombre": "CURTABLA",
                "valor": '',
                "tipo": ODBType.SYS_REFCURSOR,
                "direccion": "OUT"
            },
        ]
        ret = Oradb().execute_procedure("DBAFISICC.PKG_ACADEMICO.REQUISITOSADMISION",params)
        return ret["CURTABLA"]