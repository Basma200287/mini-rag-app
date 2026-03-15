from .BaseControler import BaseControler
from .ProjectControler import ProjectControler
import os
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyMuPDFLoader
from Models import  

class ProcessControler(BaseControler):

    def __init__(self, project_id: str):
        super().__init__()

        self.project_id = project_id
        self.project_path = ProcessControler().get_project_path(project_id)

    def get_file_extension(self, file_id: str):
        return os.path.splitext(file_id)[-1]
    
    def get_file_loader(self, file_id: str):

        file_ext = self.get_file_extension(file_id=file_id)

        #if file_ext==



    
        
