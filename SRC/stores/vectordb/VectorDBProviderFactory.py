from .providers import QdrantDBProvider
from .VectorDBEnums import VectorDBEnums
from controlers.BaseControler import BaseControler
class VectorDBProviderFactory:

    def __init__(self, config ):
        self.config= config 
        self.base_controler = BaseControler()

    def create(self, provider: str):
        if provider == VectorDBEnums.QDRANT.value:
            db_path = self.base_controler.get_database_path(db_name=self.config.VECTOR_DB_PATH)

            return QdrantDBProvider(
                db_path=db_path,
                distance_method=self.config.VECTOR_DB_DISTANCE_METHOD,
            )
        
        return None 
        
        