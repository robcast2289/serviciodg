import platform
import json
import pandas as pd
from fastapi import APIRouter, Depends, Response, HTTPException, Request, status
from fastapi.responses import JSONResponse
from models.pkg_digitalizacion import PkgDigitalizacion
from schemas.ArchivosSchema import ArchivosRequest,ArchivoResult,EtiquetasRequest, ArchivosPostRequest
from schemas.EtiquetasSchema import Etiqueta
from utils.UsuarioUtil import UsuarioUtil
from utils.settings import Settings

router = APIRouter(
    prefix="/archivos",
    tags=["Archivos"],
)

settings = Settings()

@router.get("/")
async def archivos(model:ArchivosRequest = Depends()):
    ret = PkgDigitalizacion.Archivo(model.ID)[0]

    archivo = ArchivoResult(Ruta=ret["Ruta"],Nombre=ret["Nombre"],Extension=ret["Extension"],Extencionfisica=ret["Extencionfisica"])

    if not archivo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Archivo no encontrado")


    # Obtener el archivo
    archivo_ruta = archivo.Ruta
    if(platform.system() == "Darwin" or platform.system() == "Linux"):
        archivo_ruta = archivo_ruta[2:].replace("\\","/")
        path = settings.main_path + archivo_ruta + "/" + str(model.ID) + "." + archivo.Extencionfisica
    else: 
        #platform.system() == "Windows"
        path = archivo_ruta + "\\" + str(model.ID) + "." + archivo.Extencionfisica

    try:
        with open(path, "rb") as file:
            file_content = file.read()
    except IOError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al leer el archivo")

    content_type = archivo.Extension
    headers = {
        "Content-Disposition": f"attachment; filename={archivo.Nombre}",
        "Content-Type": content_type,
    }

    return Response(content=file_content, headers=headers)


@router.get("/etiquetas")
async def etiquetas(model:EtiquetasRequest = Depends()):
    if not model.IDArchivo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="IDArchivo no proporcionado")
    
    ret = PkgDigitalizacion.EtiquetasArchivo(model.IDArchivo)
    return ret


@router.post("/")
async def archivos_post(request: Request, user:str = Depends(UsuarioUtil.get_user)):
    # Accede a los datos del cuerpo (body) de la solicitud
    form = await request.form()

    # Separa el modelo de datos de los archivos
    archivos = list()
    for campo, valor in form.items():
        if(campo == "model"):
            jsonModel = json.loads(valor)
            etiquetas_obj = []
            for etiqueta in jsonModel["Etiquetas"]:
                etiquetas_obj.append(Etiqueta(Etiqueta=etiqueta["Etiqueta"], Valor=etiqueta["Valor"]))

            model = ArchivosPostRequest(Aplicacion=jsonModel["Aplicacion"],
                                        Categoria=int(jsonModel["Categoria"]),
                                        Etiquetas=etiquetas_obj,
                                        Agregar=bool(jsonModel["Agregar"]))
        else:
            archivos.append(form.get(campo))

    # Obtiene los archivos tipo imagen o sino el archivo de aplicacion aceptada
    files = [file for file in archivos if file.content_type == 'image/bmp']
    if(len(files) > 0):
        return
    else:
        allowed_content_types = [
            'application/pdf',
            'image/tiff'
            'image/png',
            'application/msword',
            'application/vnd.ms-excel',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        ]
        file = [file for file in archivos if file.content_type in allowed_content_types][0]

        if not file:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Debe ingresar un archivo")

    # Obtener informacion del archivo
    file_ext = file.filename.split(".").pop()
    file_content = await file.read()
    file_length = len(file_content)
    file_content_type = file.content_type

    if not file_ext:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Falta Extencion en el archivo")

    # Construye el nombre del archivo
    query_tags = [str(a.Valor) for a in model.Etiquetas]
    file_name = "-".join(query_tags) + "." + file_ext 

    # Obtiene las rutas segun aplicacion y categoria del servidor
    ruta = PkgDigitalizacion.Rutacategoria(model.Aplicacion,model.Categoria)
    ruta = ruta.replace("\\\\","\\")

    print(ruta)
    try:
        # Verifica repetido
        if(model.Agregar):
            IDArchivos = list()

            for tag in model.Etiquetas:
                _archivos = PkgDigitalizacion.Idarchivo(model.Aplicacion,model.Categoria,tag.Etiqueta,tag.Valor)
                IDArchivos.append(_archivos)

            # Transforma la lista de listas en una sola lista
            IDArchivos_flat = [item for sublist in IDArchivos for item in sublist]
            # Convertir las listas en DataFrames,Realizar el agrupamiento y filtro,Obtener los valores agrupados que cumplen con la condición
            query = pd.DataFrame(IDArchivos_flat, columns=['IDArchivo']).groupby('IDArchivo').filter(lambda x: x['IDArchivo'].count() == len(model.Etiquetas))['IDArchivo'].unique().tolist()

            if(len(query) > 0):
                noversion = PkgDigitalizacion.Version(query[0])
                PkgDigitalizacion.Actualizararchivonovalido(query[0])
        # Fin verifica repetido
        
        IDArchivo:int
        aws = settings.save_aws

        
        while True:
            IDArchivo = PkgDigitalizacion.Idarchivonuevo()
            print(IDArchivo)
            PkgDigitalizacion.Insertararchivo(IDArchivo,file_name,file_length,file_content_type,user,noversion,ruta,file_ext)
            archivo = file_name.split(".")[0]

            for tag in model.Etiquetas:
                PkgDigitalizacion.Insertardetallearchivo(IDArchivo,model.Aplicacion,model.Categoria,tag.Etiqueta,tag.Valor)

            # Arma la ruta final segun sistema operativo o almacenamiento
            if(platform.system() == "Darwin" or platform.system() == "Linux" or aws == True):
                archivo_ruta = ruta[2:].replace("\\","/")
                path = settings.main_path + archivo_ruta + "/" + str(IDArchivo) + "." + file_ext
            else: 
                path = ruta + "\\" + str(IDArchivo) + "." + file_ext
            print(path)
            print(aws)
            if not aws:
                print("Entro local")
                # graba en SO local                
                with open(path,"wb") as f:
                    content = await file.read()
                    f.write(content)
            else:
                print("Entro aws")
                # graba en AWS
                pass


            # Etiquetando
            if(model.Aplicacion == "TI" and (model.Categoria == 6 or model.Categoria == 7) and len([a for a in model.Etiquetas if a.Etiqueta == 4]) > 0):
                model.Aplicacion = "SO"
                model.Categoria = 5
                model.Etiquetas = [a for a in model.Etiquetas if a.Etiqueta == 4]
                ruta = PkgDigitalizacion.Rutacategoria(model.Aplicacion,model.Categoria)
            else:
                break
        
        return IDArchivo
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
    ##################
    """ file_path = f"/Users/robertocastro/FileTest/prestaciones2/expedienteadm2023/{file_name}.{file_ext}"
    with open(file_path,"wb") as f:
        content = await file.read()
        f.write(content) """
    
    #return JSONResponse(content={"resultado": "Datos recibidos y procesados"})
    

@router.post("/aws")
async def aws():
    aws = bool(settings.save_aws)
    return aws