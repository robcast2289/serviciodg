from repositories.oracle.ora_db import Oradb, ODBType, ODBFunctionType

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
        return ret["CURTABLA"]
    

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


    def Entidad(Carrera:str):
        params = [
            {
                "nombre": "PCARRERA",
                "tipo": ODBType.DECIMAL,
                "valor": Carrera,
                "direccion": "IN"
            },
        ]
        ret = Oradb().execute_function("DBAFISICC.PKG_DIGITALIZACION.ENTIDAD",params,ODBFunctionType.STRING)
        return ret["RETORNO_FUNCION"]


    def Obtenertitulosxcarrera(Carrera:str ,Titulo:int):
        params = [
            {
                "nombre": "PCARRERA",
                "tipo": ODBType.VARCHAR2,
                "valor": Carrera,
                "direccion": "IN"
            },
            {
                "nombre": "PTITULO",
                "tipo": ODBType.INT,
                "valor": Titulo,
                "direccion": "IN"
            },
            {
                "nombre": "CURTABLA",
                "tipo": ODBType.SYS_REFCURSOR,
                "valor": '',
                "direccion": "OUT"
            },
        ]
        ret = Oradb().execute_procedure("DBAFISICC.PKG_DIGITALIZACION.OBTENERTITULOSXCARRERA",params)
        return ret["CURTABLA"]
    

    def Rutacategoria(Aplicacion:str, Categoria:int):
        params = [
            {
                "nombre": "PAPLICACION",
                "tipo": ODBType.VARCHAR2,
                "valor": Aplicacion,
                "direccion": "IN"
            },
            {
                "nombre": "PCATEGORIA",
                "tipo": ODBType.INT,
                "valor": Categoria,
                "direccion": "IN"
            },
        ]
        ret = Oradb().execute_function("DBAFISICC.PKG_DIGITALIZACION.RUTACATEGORIA",params,ODBFunctionType.STRING)
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
        retProc = ret["CURTABLA"]
        lst = list()
        for alumno in retProc:
            lst.append(alumno["Nombrealumno"])
        return lst
    

    def Idarchivo(Aplicacion:str, Categoria:int, Etiqueta:int, Valor:str):
        params = [
            {
                "nombre": "PAPLICACION",
                "tipo": ODBType.VARCHAR2,
                "valor": Aplicacion,
                "direccion": "IN"
            },
            {
                "nombre": "PCATEGORIA",
                "tipo": ODBType.INT,
                "valor": Categoria,
                "direccion": "IN"
            },            
            {
                "nombre": "PETIQUETA",
                "tipo": ODBType.INT,
                "valor": Etiqueta,
                "direccion": "IN"
            },            
            {
                "nombre": "PVALOR",
                "tipo": ODBType.VARCHAR2,
                "valor": Valor,
                "direccion": "IN"
            },
        ]
        ret = Oradb().execute_function("DBAFISICC.PKG_DIGITALIZACION.IDARCHIVO",params,ODBFunctionType.CURSOR)
        retFunc = ret["RETORNO_FUNCION"]
        lst = list()
        for link in retFunc:
            lst.append(link["Idarchivo"])
        return lst
    

    def Actualizararchivonovalido(Idarchivo:int):
        params = [
            {
                "nombre": "PIDARCHIVO",
                "tipo": ODBType.DECIMAL,
                "valor": Idarchivo,
                "direccion": "IN"
            },                    
        ]
        Oradb().execute_procedure("DBAFISICC.PKG_DIGITALIZACION.ACTUALIZARARCHIVONOVALIDO",params)
        return
    

    def Version(Idarchivo:int):
        params = [
            {
                "nombre": "PIDARCHIVO",
                "tipo": ODBType.DECIMAL,
                "valor": Idarchivo,
                "direccion": "IN"
            },            
        ]
        ret = Oradb().execute_function("DBAFISICC.PKG_DIGITALIZACION.VERSION",params,ODBFunctionType.NUMBER)
        return ret["RETORNO_FUNCION"]
    

    def Insertardetallearchivo(Idarchivo:int, Aplicacion:str, Categoria:int, Etiqueta:int, Valor:str):
        params = [
            {
                "nombre": "PIDARCHIVO",
                "tipo": ODBType.DECIMAL,
                "valor": Idarchivo,
                "direccion": "IN"
            },
            {
                "nombre": "PAPLICACION",
                "tipo": ODBType.VARCHAR2,
                "valor": Aplicacion,
                "direccion": "IN"
            }, 
            {
                "nombre": "PCATEGORIA",
                "tipo": ODBType.INT,
                "valor": Categoria,
                "direccion": "IN"
            }, 
            {
                "nombre": "PETIQUETA",
                "tipo": ODBType.INT,
                "valor": Etiqueta,
                "direccion": "IN"
            }, 
            {
                "nombre": "PVALOR",
                "tipo": ODBType.VARCHAR2,
                "valor": Valor,
                "direccion": "IN"
            }, 
        ]
        ret = Oradb().execute_procedure("DBAFISICC.PKG_DIGITALIZACION.INSERTARDETALLEARCHIVO",params)
        return
    

    def Idarchivonuevo():
        params = []
        ret = Oradb().execute_function("DBAFISICC.PKG_DIGITALIZACION.IDARCHIVO_NUEVO",params,ODBFunctionType.NUMBER)
        return ret["RETORNO_FUNCION"]
    

    def Insertararchivo(Idarchivo:int, Nombre:str, Tamano:float, Extension:str, Usuario:str, Noversion:int, Ruta:str, Extensionfisica:str):
        params = [
            {
                "nombre": "PIDARCHIVO",
                "tipo": ODBType.DECIMAL,
                "valor": Idarchivo,
                "direccion": "IN"
            },    
            {
                "nombre": "PNOMBRE",
                "tipo": ODBType.VARCHAR2,
                "valor": Nombre,
                "direccion": "IN"
            },
            {
                "nombre": "PTAMANO",
                "tipo": ODBType.DECIMAL,
                "valor": Tamano,
                "direccion": "IN"
            },
            {
                "nombre": "PEXTENSION",
                "tipo": ODBType.VARCHAR2,
                "valor": Extension,
                "direccion": "IN"
            },
            {
                "nombre": "PUSUARIO",
                "tipo": ODBType.VARCHAR2,
                "valor": Usuario,
                "direccion": "IN"
            },
            {
                "nombre": "PNOVERSION",
                "tipo": ODBType.INT,
                "valor": Noversion,
                "direccion": "IN"
            },
            {
                "nombre": "PRUTA",
                "tipo": ODBType.VARCHAR2,
                "valor": Ruta,
                "direccion": "IN"
            },
            {
                "nombre": "PEXTENCIONFISICA",
                "tipo": ODBType.VARCHAR2,
                "valor": Extensionfisica,
                "direccion": "IN"
            },        
        ]
        ret = Oradb().execute_procedure("DBAFISICC.PKG_DIGITALIZACION.INSERTARARCHIVO",params)
        return 

    

    def Archivovalido(Idarchivo:int):
        params = [
            {
                "nombre": "PIDARCHIVO",
                "tipo": ODBType.DECIMAL,
                "valor": Idarchivo,
                "direccion": "IN"
            }
        ]
        ret = Oradb().execute_function("DBAFISICC.PKG_DIGITALIZACION.ARCHIVOVALIDO",params,ODBFunctionType.CURSOR)
        return ret["RETORNO_FUNCION"]
    

    def Nombrecarreras(Carrera:str):
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
                "tipo": ODBType.SYS_REFCURSOR,
                "valor": '',
                "direccion": "OUT"
            },
            {
                "nombre": "PCARRERA",
                "tipo": ODBType.VARCHAR2,
                "valor": Carrera,
                "direccion": "IN"
            },                        
        ]
        ret = Oradb().execute_procedure("DBAFISICC.PKG_DIGITALIZACION.BUSCARCARRERA",params)
        return ret["RETVAL"]