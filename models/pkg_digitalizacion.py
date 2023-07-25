from models.oracle.ora_db import Oradb, ODBType, ODBFunctionType

class PkgDigitalizacion:

    def AplicacionesNombre():
        params = []
        ret = Oradb().execute_function("DBAFISICC.PKG_DIGITALIZACION.APLICACIONES_NOMBRE",params,ODBFunctionType.CURSOR)
        return ret["RETORNO_FUNCION"]
    

    def Categorias(Aplicacion:str):
        params = [
            {
                "nombre": "PAPLICACION",
                "tipo": ODBType.VARCHAR2,
                "valor": Aplicacion,
                "direccion": "IN"
            },
        ]
        ret = Oradb().execute_function("DBAFISICC.PKG_DIGITALIZACION.CATEGORIAS",params,ODBFunctionType.CURSOR)
        return ret["RETORNO_FUNCION"]
    


    def Etiquetas():
        params = []
        ret = Oradb().execute_function("DBAFISICC.PKG_DIGITALIZACION.ETIQUETAS",params,ODBFunctionType.CURSOR)
        return ret["RETORNO_FUNCION"]
    

    def EtiquetasArchivo(Idarchivo:int):
        params = [
            {
                "nombre": "PIDARCHIVO",
                "tipo": ODBType.DECIMAL,
                "valor": Idarchivo,
                "direccion": "IN"
            },
        ]
        ret = Oradb().execute_function("DBAFISICC.PKG_DIGITALIZACION.ETIQUETASARCHIVO",params,ODBFunctionType.CURSOR)
        return ret["RETORNO_FUNCION"]
    

    def ResolucionesCompletas(Resolucion:str):
        params = [
            {
                "nombre": "PRESOLUCION",
                "tipo": ODBType.VARCHAR2,
                "valor": Resolucion,
                "direccion": "IN"
            },
        ]
        ret = Oradb().execute_function("DBAFISICC.PKG_DIGITALIZACION.OBTENERRESOLUCIONESCOMPLETAS",params,ODBFunctionType.CURSOR)
        return ret["RETORNO_FUNCION"]
    

    def Obtenercarrerasxcarnet(Carnet:str):
        params = [
            {
                "nombre": "PCARNET",
                "tipo": ODBType.VARCHAR2,
                "valor": Carnet,
                "direccion": "IN"
            },
            {
                "nombre": "CURTABLA",
                "valor": '',
                "tipo": ODBType.SYS_REFCURSOR,
                "direccion": "OUT"
            },
        ]
        ret = Oradb().execute_procedure("DBAFISICC.PKG_DIGITALIZACION.OBTENERCARRERASXCARNET",params)
        return ret["RETVAL"]
    

    def Archivo(Idarchivo:int):
        params = [
            {
                "nombre": "PIDARCHIVO",
                "tipo": ODBType.DECIMAL,
                "valor": Idarchivo,
                "direccion": "IN"
            },
        ]
        ret = Oradb().execute_function("DBAFISICC.PKG_DIGITALIZACION.ARCHIVO",params,ODBFunctionType.CURSOR)
        return ret["RETORNO_FUNCION"]


    def Obtenernombrealumno(Carnet:str):
        params = [
            {
                "nombre": "PCARNET",
                "tipo": ODBType.VARCHAR2,
                "valor": Carnet,
                "direccion": "IN"
            },
            {
                "nombre": "CURTABLA",
                "tipo": ODBType.SYS_REFCURSOR,
                "valor": '',
                "direccion": "OUT"
            },
        ]
        ret = Oradb().execute_procedure("DBAFISICC.PKG_DIGITALIZACION.OBTENERNOMBREALUMNO",params)
        return ret["CURTABLA"]