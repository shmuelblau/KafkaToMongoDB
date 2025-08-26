from models.dbloader import DBLoader
from models.consumer import Consumer
from datetime import datetime
from models.logger import get_logger
log = get_logger()
class Manager:
    
    def __init__(self , connection_string , db_name ,collection ,kafka_host ) -> None:

        self.db:DBLoader = DBLoader(connection_string ,db_name , collection )
        self.consumer:Consumer = Consumer(kafka_host , collection)
    
    def start(self):

        data:list = self.consumer.get_data()

        log.info(f"get a data from kafka type:{type(data)} len:{len(data)} type[0]:{type(data[0])} ")

        data = [Manager.add_time(line) for line in data]
        log.info(f"add time type[0]:{type(data[0])} len:{len(data)} ")
        self.db.insert(data)

        return data
    







    @staticmethod
    def add_time(text):

        return {"data":text , "time": str(datetime.now())}

    

