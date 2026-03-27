from pydantic import BaseModel, Field, validator, field_validator
from typing import Optional
from bson.objectid import ObjectId

class DataChunk(BaseModel):
    id: Optional[ObjectId]= Field(None, alias="_id")
    chunk_text: str = Field(...,min_length=1)
    chunk_metadata: dict 
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectId
    
    @field_validator("chunk_project_id", mode="before")
    def convert_objectid(cls, v):
        if isinstance(v, ObjectId):
            return v
        return ObjectId(v)  

    model_config = {
        "arbitrary_types_allowed": True
    }

    @classmethod
    def get_indexes(cls):

        return [
            {
                "key": [
                    ("chunk_project_id", 1)
                ],
                "name": "chunk_project_id_index_1",
                "unique": False
            }
        ]
