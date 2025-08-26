
from models.dataloader import DataLoader
from models.logger import get_logger
from models.Producer import Producer


log = get_logger()
class Manager:

    def __init__(self , host) -> None:

        self.producer:Producer = Producer(host)
        
        self.all_data: dict[str , list] = DataLoader.get_all()

    def send_to_kafka(self , limit = 20)-> None:

        data:dict[str , list]  = self.get_masages(limit)

        log.info(f"data to send = interesting:{len(data['interesting'])} not_interesting:{len(data['not_interesting'])} ")

        self.producer.send_all(data)


    def get_masages(self , count) -> dict[str , list]:
        count = count // 2 
        result = {}

        for topic , data in self.all_data.items():
            result[topic] = data[0:count]
            data = data[count:-1]

        return result






    

