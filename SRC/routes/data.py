from fastapi import APIRouter, Depends, UploadFile, status,  Request
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
from Models.ProjectModel import ProjectModel
from Models.db_schemes import DataChunk
from Models.ChunkModel import ChunkModel
from bson import ObjectId

logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(request: Request, project_id:str,file:UploadFile, 
                      app_settings:Settings = Depends(get_settings)):


                      project_model= ProjectModel(
                        db_client= request.app.db_client
                      )
                      project = await project_model.get_project_or_create_one(
                        project_id=project_id
                      )


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
async def process_endpoint(request: Request, project_id: str, process_request: ProcessRequest ):

    file_id = process_request.file_id

    process_controler = ProcessControler(project_id=project_id)

    file_content = process_controler.get_file_content(file_id=file_id)

    chunk_size = process_request.chunk_size
    overlap_size = process_request.overlap_size
    do_reset = process_request.do_reset

    project_model= ProjectModel(
        db_client= request.app.db_client
        )
    project = await project_model.get_project_or_create_one(
        project_id=project_id
        )

        
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
    
    file_chunks_records = [
        DataChunk(
            chunk_text=chunk.page_content,
            chunk_metadata=chunk.metadata,
            chunk_order=i+1,
            chunk_project_id = project.id if hasattr(project, "_id") else ObjectId(project.id)
        )
        for i, chunk in enumerate(file_chunks)
    ]
    
    chunk_model = ChunkModel(
        db_client= request.app.db_client
    )

    if do_reset == 1:
        _ = await chunk_model.delete_chunks_by_project_id(
            project_id=project.id
        )

    no_records = await chunk_model.insert_many_chunks(chunks=file_chunks_records)

    return JSONResponse(
        content={
            "signal": ResponseSignal.PROCESSING_SUCCESS.value,
            "inserted_chunks":no_records
        }    
    ) 
    

                                



