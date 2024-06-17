from mictlanx.v4.client import Client
from mictlanx.utils.index import Utils as UtilsX
from dotenv import load_dotenv
import os
ENV_FILE_PATH = os.environ.get("ENV_FILE_PATH",-1)
if not ENV_FILE_PATH == -1:
    load_dotenv(ENV_FILE_PATH)


MICTLANX_CLIENT_ID         = os.environ.get("MICTLANX_CLIENT_ID","client-0")
MICTLANX_DEFAULT_BUCKET_ID = os.environ.get("MICTLANX_DEFAULT_BUCKET_ID","moringas")
MICTLANX_DEBUG             = bool(int(os.environ.get("MICTLANX_DEBUG","1")))
MICTLANX_MAX_WORKERS       = int(os.environ.get("MICTLANX_MAX_WORKERS","2"))
MICTLANX_LOG_PATH          = os.environ.get("MICTLANX_LOG_PATH","./log")
SOURCE_PATH                = os.environ.get("SOURCE_PATH","./source")
routers = list(UtilsX.routers_from_str(os.environ.get("MICTLANX_ROUTERS","mictlanx-router-0:localhost:60666")))
client = Client(
    client_id      = MICTLANX_CLIENT_ID,
    routers         = routers,
    debug           = MICTLANX_DEBUG,
    max_workers     = MICTLANX_MAX_WORKERS,
    bucket_id       = MICTLANX_DEFAULT_BUCKET_ID,
    log_output_path = MICTLANX_LOG_PATH    
)
def subir_archivo_desde_tu_disco_pedorro(
        path:str, 
        bucket_id:str = MICTLANX_DEFAULT_BUCKET_ID,
        key:str="",
        chunk_size:str="1MB"
):
    """
        path: It is the real path of the data 
        bucket_id: It is the unique identifier of the bucket(cubeta)
        key: It is a unique identifier if you let empty it is assign to the sha256(bytes)
        chunk_size: It is the size of the data chunks 
    """
    if os.path.exists(path):
        print("Subiendo la imagen en la ruta: {}".format(path))
        res= client.put_file_chunked(path=path,chunk_size=chunk_size,bucket_id=bucket_id,key=key)
        if res.is_ok:
            put_file_chunked_response = res.unwrap() # You must unwrap the result
            print("Se subio correctamente al sistema de almacenamiento en la cubeta {} con la llave {}".format(put_file_chunked_response.bucket_id,put_file_chunked_response.key))
            print("_"*40)
            return put_file_chunked_response.key
        else:
            print("Hubo un error :( ay que llorar")
            print("el error es {}".format(str(res.unwrap_err())))
            print("_"*40)


def main():
    path1 = "{}/01.gif".format(SOURCE_PATH)
    res1 = subir_archivo_desde_tu_disco_pedorro(path=path1)
    path2 = "{}/02.jpg".format(SOURCE_PATH)
    res2 = subir_archivo_desde_tu_disco_pedorro(path=path2)
    path3 = "{}/03.jpg".format(SOURCE_PATH)
    res3 = subir_archivo_desde_tu_disco_pedorro(path=path3)

if __name__ == "__main__":
    main()