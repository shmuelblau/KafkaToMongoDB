from models.dbloader import DBLoader
from models.consumer import Consumer
from time import time
class Manager:
    
    def __init__(self , connection_string , db_name ,collection ,kafka_host ) -> None:

        self.db:DBLoader = DBLoader(connection_string ,db_name , collection )
        self.consumer:Consumer = Consumer(kafka_host , collection)
    
    def start(self):

        data:list = self.consumer.get_data()

        data = [Manager.add_time(line) for line in data]

        self.db.insert(data)

        return data







    @staticmethod
    def add_time(text):

        return {"data":text , "time": time.time}

    

