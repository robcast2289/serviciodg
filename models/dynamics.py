from repositories.sqlserver.sql_db import Sqldb

class Dynamics:
    def ObtenerNombre(emplId:str):
        query = f"EXEC Obtener_Nombre '{emplId}'"
        ret = Sqldb().execute_query(query)
        try:
            nombre = ret[0]["Name"]
            return nombre
        except Exception:
            Exception("El empleado no ha sido encontrado")
         