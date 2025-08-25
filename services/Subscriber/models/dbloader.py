from pymongo import MongoClient
from pymongo.database import Database
from time import time
from models.logger import get_logger

log = get_logger()


class DBLoader:


    def __init__(self ,connection_string ,db_name , collection  ) -> None:
        self.db:Database = DAL(connection_string , db_name).get_conn()

        self.collection = collection

# -----------------------------------------------------------------------------------

    def insert(self , data:list) -> None:

        
        log.info(f"start load data len ={len(data)}")

        try:
            
            self.db[self.collection].insert_many(data)
            log.info("load finish")

        except Exception as e:
            log.info("insert failed")
            log.info(f"type error {e}")


# =================================================================================

class DAL:
    def __init__(self ,connection_string , db_name ) -> None:

         myclient = MongoClient(connection_string)
         self.conn = myclient[db_name]
          
        
           
    def get_collections(self) -> list:
        return self.conn.list_collection_names()
    

    def get_conn(self) -> Database:
        
        return self.conn 