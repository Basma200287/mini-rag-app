from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controlers.DataControler import DataControler
from controlers.ProjectControler import ProjectControler
import aiofiles
from Models import ResponseSignal


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
                     file_path = data_controler.generate_unique_filename(
                        orig_file_name = file.orig_file_name,
                        project_id = project_id
                     )


                     # save file chunks
                     async with aiofiles.open(file_path, "wb") as f :
                        while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                            await f.write(chunk) 

               
                     return JSONResponse(
                            content = {
                                "signal" : ResponseSignal.FILE_UPLOADED_SUCCESS.value
                                }
                        )
                                



