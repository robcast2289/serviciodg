from models.oracle.ora_db import Oradb, ODBType, ODBFunctionType

class PkgEncabezado:
    def Facultad(Usuario:str, Universidad:str, Activas:int = 0, Incluye_Idea:int = 0, Todos:int = 0):
        params = [
            {
                "nombre": "PUSUARIO",
                "tipo": ODBType.VARCHAR2,
                "valor": Usuario,
                "direccion": "IN"
            },
            {
                "nombre": "PUNIVERSIDAD",
                "tipo": ODBType.VARCHAR2,
                "valor": Universidad,
                "direccion": "IN"
            },
            {
                "nombre": "PACTIVAS",
                "tipo": ODBType.DECIMAL,
                "valor": Activas,
                "direccion": "IN"
            },
            {
                "nombre": "PINCLUYE_IDEA",
                "tipo": ODBType.DECIMAL,
                "valor": Incluye_Idea,
                "direccion": "IN"
            },
            {
                "nombre": "PTODOS",
                "tipo": ODBType.DECIMAL,
                "valor": Todos,
                "direccion": "IN"
            },
            {
                "nombre": "RETVAL",
                "valor": '',
                "tipo": ODBType.SYS_REFCURSOR,
                "direccion": "OUT"
            },
        ]

        result = Oradb().execute_procedure("DBAFISICC.PKG_ENCABEZADO.FACULTAD",params)

        return result["RETVAL"]