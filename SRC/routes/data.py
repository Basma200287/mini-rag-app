from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controlers.DataControler import DataControler
from controlers.ProjectControler import ProjectControler
from controlers.ProcessControler import ProcessControler
import aiofiles
from Models import ResponseSignal
import logging
from .schemes.data import ProcessRequest


logger = logging.getLogger('uvicorn.error')



data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id:str,file:UploadFile, 
                      app_settings:Settings = Depends(get_settings)):

                     #validate the file proprieties
                     data_controler = DataControler()


                     is_valid, result_signal = data_controler.validate_uploaded_file(file=file)
                     
                     if not is_valid:
                        return JSONResponse(
                            status_code = status.HTTP_400_BAD_REQUEST,
                            content = {
                                "signal" :result_signal
                            }
                        )

                     #create project folder
                     project_dir_path = ProjectControler().get_project_path(project_id=project_id)
                     file_path, file_id = data_controler.generate_unique_filepath(
                        orig_file_name = file.filename,
                        project_id = project_id
                     )


                     # save file chunks
                     try:
                        async with aiofiles.open(file_path, "wb") as f :
                            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                                await f.write(chunk) 
                     except Exception as e:

                        logger.error(f"Error while uploading file: {e}")                     

                        return JSONResponse(
                            status_code = status.HTTP_400_BAD_REQUEST,
                            content = {
                                "signal" : ResponseSignal.FILE_UPLOADED_FAILED.value
                            }
                        )
               
                     return JSONResponse(
                            content = {
                                "signal" : ResponseSignal.FILE_UPLOADED_SUCCESS.value,
                                "file_id": file_id
                                }
                        )


@data_router.post("/process/{project_id}")
async def process_endpoint(project_id: str, process_request: ProcessRequest ):

    file_id = process_request.file_id

    process_controler = ProcessControler(project_id=project_id)

    file_content = process_controler.get_file_content(file_id=file_id)

    chunk_size = process_request.chunk_size
    overlap_size = process_request.overlap_size

    
    file_chunks = process_controler.process_file_content(
        file_content=file_content,
        file_id=file_id,
        chunk_size=chunk_size,
        overlap_size=overlap_size
    )

    if file_chunks is None or len(file_chunks) == 0:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {
            "signal" : ResponseSignal.PROSSECING_FAILED.value
            }
        )
    

    return file_chunks

                                



