from models.oracle.ora_db import Oradb, ODBType, ODBFunctionType

class PkgCI:
    def AutenticarAdministrativo(Usuario: str, Contrasena: str):
        params = [
            {
                "nombre": "PUSUARIO",
                "valor": Usuario,
                "tipo": ODBType.VARCHAR2,
                "direccion": "IN"
            },
            {
                "nombre": "PCONTRASENA",
                "valor": Contrasena,
                "tipo": ODBType.VARCHAR2,
                "direccion": "IN"
            }
        ]

        result = Oradb().execute_function("DBAFISICC.PKG_CI.AUTENTICARADMINISTRATIVO",params,ODBFunctionType.NUMBER)

        return result["RETORNO_FUNCION"]