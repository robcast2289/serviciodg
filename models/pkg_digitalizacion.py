from repositories.oracle.ora_db import Oradb, ODBType, ODBFunctionType

class PkgDigitalizacion(Oradb):
    def __init__(self):
        super().__init__()

    def AplicacionesNombre(self):
        params = []
        ret = self.execute_function("DBAFISICC.PKG_DIGITALIZACION.APLICACIONES_NOMBRE",params,ODBFunctionType.CURSOR)
        return ret["RETORNO_FUNCION"]
    

    def Categorias(self,Aplicacion:str):
        params = [
            {
                "nombre": "PAPLICACION",
                "tipo": ODBType.VARCHAR2,
                "valor": Aplicacion,
                "direccion": "IN"
            },
        ]
        ret = self.execute_function("DBAFISICC.PKG_DIGITALIZACION.CATEGORIAS",params,ODBFunctionType.CURSOR)
        return ret["RETORNO_FUNCION"]
    


    def Etiquetas(self):
        params = []
        ret = self.execute_function("DBAFISICC.PKG_DIGITALIZACION.ETIQUETAS",params,ODBFunctionType.CURSOR)
        return ret["RETORNO_FUNCION"]
    

    def EtiquetasArchivo(self,Idarchivo:int):
        params = [
            {
                "nombre": "PIDARCHIVO",
                "tipo": ODBType.DECIMAL,
                "valor": Idarchivo,
                "direccion": "IN"
            },
        ]
        ret = self.execute_function("DBAFISICC.PKG_DIGITALIZACION.ETIQUETASARCHIVO",params,ODBFunctionType.CURSOR)
        return ret["RETORNO_FUNCION"]
    

    def ResolucionesCompletas(self,Resolucion:str):
        params = [
            {
                "nombre": "PRESOLUCION",
                "tipo": ODBType.VARCHAR2,
                "valor": Resolucion,
                "direccion": "IN"
            },
        ]
        ret = self.execute_function("DBAFISICC.PKG_DIGITALIZACION.OBTENERRESOLUCIONESCOMPLETAS",params,ODBFunctionType.CURSOR)
        return ret["RETORNO_FUNCION"]
    

    def Obtenercarrerasxcarnet(self,Carnet:str):
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
        ret = self.execute_procedure("DBAFISICC.PKG_DIGITALIZACION.OBTENERCARRERASXCARNET",params)
        return ret["CURTABLA"]
    

    def Archivo(self,Idarchivo:int):
        params = [
            {
                "nombre": "PIDARCHIVO",
                "tipo": ODBType.DECIMAL,
                "valor": Idarchivo,
                "direccion": "IN"
            },
        ]
        ret = self.execute_function("DBAFISICC.PKG_DIGITALIZACION.ARCHIVO",params,ODBFunctionType.CURSOR)
        return ret["RETORNO_FUNCION"]


    def Entidad(self,Carrera:str):
        params = [
            {
                "nombre": "PCARRERA",
                "tipo": ODBType.DECIMAL,
                "valor": Carrera,
                "direccion": "IN"
            },
        ]
        ret = self.execute_function("DBAFISICC.PKG_DIGITALIZACION.ENTIDAD",params,ODBFunctionType.STRING)
        return ret["RETORNO_FUNCION"]


    def Obtenertitulosxcarrera(self,Carrera:str ,Titulo:int):
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
        ret = self.execute_procedure("DBAFISICC.PKG_DIGITALIZACION.OBTENERTITULOSXCARRERA",params)
        return ret["CURTABLA"]
    

    def Rutacategoria(self,Aplicacion:str, Categoria:int):
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
        ret = self.execute_function("DBAFISICC.PKG_DIGITALIZACION.RUTACATEGORIA",params,ODBFunctionType.STRING)
        return ret["RETORNO_FUNCION"]


    def Obtenernombrealumno(self,Carnet:str):
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
        ret = self.execute_procedure("DBAFISICC.PKG_DIGITALIZACION.OBTENERNOMBREALUMNO",params)
        retProc = ret["CURTABLA"]
        lst = list()
        for alumno in retProc:
            lst.append(alumno["Nombrealumno"])
        return lst
    

    def Idarchivo(self,Aplicacion:str, Categoria:int, Etiqueta:int, Valor:str):
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
        ret = self.execute_function("DBAFISICC.PKG_DIGITALIZACION.IDARCHIVO",params,ODBFunctionType.CURSOR)
        retFunc = ret["RETORNO_FUNCION"]
        lst = list()
        for link in retFunc:
            lst.append(link["Idarchivo"])
        return lst
    

    def Actualizararchivonovalido(self,Idarchivo:int):
        params = [
            {
                "nombre": "PIDARCHIVO",
                "tipo": ODBType.DECIMAL,
                "valor": Idarchivo,
                "direccion": "IN"
            },                    
        ]
        self.execute_procedure("DBAFISICC.PKG_DIGITALIZACION.ACTUALIZARARCHIVONOVALIDO",params)
        return
    

    def Version(self,Idarchivo:int):
        params = [
            {
                "nombre": "PIDARCHIVO",
                "tipo": ODBType.DECIMAL,
                "valor": Idarchivo,
                "direccion": "IN"
            },            
        ]
        ret = self.execute_function("DBAFISICC.PKG_DIGITALIZACION.VERSION",params,ODBFunctionType.NUMBER)
        return ret["RETORNO_FUNCION"]
    

    def Insertardetallearchivo(self,Idarchivo:int, Aplicacion:str, Categoria:int, Etiqueta:int, Valor:str):
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
        ret = self.execute_procedure("DBAFISICC.PKG_DIGITALIZACION.INSERTARDETALLEARCHIVO",params)
        return
    

    def Idarchivonuevo(self,):
        params = []
        ret = self.execute_function("DBAFISICC.PKG_DIGITALIZACION.IDARCHIVO_NUEVO",params,ODBFunctionType.NUMBER)
        return ret["RETORNO_FUNCION"]
    

    def Insertararchivo(self,Idarchivo:int, Nombre:str, Tamano:float, Extension:str, Usuario:str, Noversion:int, Ruta:str, Extensionfisica:str):
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
        ret = self.execute_procedure("DBAFISICC.PKG_DIGITALIZACION.INSERTARARCHIVO",params)
        return 

    

    def Archivovalido(self,Idarchivo:int):
        params = [
            {
                "nombre": "PIDARCHIVO",
                "tipo": ODBType.DECIMAL,
                "valor": Idarchivo,
                "direccion": "IN"
            }
        ]
        ret = self.execute_function("DBAFISICC.PKG_DIGITALIZACION.ARCHIVOVALIDO",params,ODBFunctionType.CURSOR)
        return ret["RETORNO_FUNCION"]
    

    def Nombrecarreras(self,Carrera:str):
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
        ret = self.execute_procedure("DBAFISICC.PKG_DIGITALIZACION.BUSCARCARRERA",params)
        return ret["RETVAL"]