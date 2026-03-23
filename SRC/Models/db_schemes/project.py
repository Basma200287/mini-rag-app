from pydantic import BaseModel
from typing import Optional
from bson.objecteid import ObjectId

class Project(BaseModel):
    _id: Optional[ObjectId] 
    project_id: str =nfield(...,min_length=1)

    