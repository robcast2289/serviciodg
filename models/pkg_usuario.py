from repositories.oracle.ora_db import Oradb, ODBType, ODBFunctionType
from typing import List

class PkgUsuario:
    def Linksdigitalizacion(Usuario: str):
        params = [
            {
                "nombre": "PUSUARIO",
                "tipo": ODBType.VARCHAR2,
                "valor": Usuario,
                "direccion": "IN"
            }
        ]

        result = Oradb().execute_function("DBAFISICC.PKG_USUARIO.LINKSDIGITALIZACION",params,ODBFunctionType.CURSOR)
        resultFunc = result["RETORNO_FUNCION"]
        lst = list()
        for link in resultFunc:
            lst.append(link["Link"])


        return lst